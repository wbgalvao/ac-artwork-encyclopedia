import click
import psycopg2
import requests

from bs4 import BeautifulSoup
from flask import current_app
from flask import g
from flask.cli import with_appcontext


def get_db():
    if "db" not in g:
        g.db = psycopg2.connect(current_app.config["DATABASE_CONNECTION_URI"])
    return g.db


def close_db(e=None):
    db = g.pop("db", None)
    if db is not None:
        db.close()


def init_db():
    db = get_db()
    cur = db.cursor()

    with current_app.open_resource("schema.sql") as f:
        cur.execute(f.read().decode("utf-8"))
        db.commit()
        f.close()

    response = requests.get(current_app.config["DATASOURCE_URL"])
    soup = BeautifulSoup(response.content, "html.parser")
    complete_list_of_paintings = soup.find("h2", string="Complete List of Paintings").find_next_sibling().find_all("li")
    complete_list_of_statues = soup.find("h2", string="Complete List of Statues").find_next_sibling().find_all("li")
    complete_list_of_artworks = complete_list_of_paintings + complete_list_of_statues

    for artwork in complete_list_of_artworks:
        animal_crossing_name = artwork.text.strip()
        artwork_url = artwork.a["href"]
        artwork_element_id = artwork_url[artwork_url.find("#") + 1 :]
        artwork_real_name, artwork_real_author = soup.find(id=artwork_element_id).find_next_sibling().find("strong").text.lstrip("(").rstrip(")").split(" by ")
        difference = soup.find(id=artwork_element_id).find_next("p").text
        image_url = soup.find(id=artwork_element_id).find_next("img")["src"]
        cur.execute(
            """INSERT INTO artwork (animal_crossing_name, real_life_name, real_life_author, authenticity_helper_info, polygon_image_url)
            VALUES (%s, %s, %s, %s, %s)""",
            (animal_crossing_name, artwork_real_name, artwork_real_author, difference, image_url,)
        )
        db.commit()

    cur.close()
    db.close()



@click.command("init-db")
@with_appcontext
def init_db_command():
    init_db()
    click.echo(" * Initialized database")


def init_app(app):
    app.teardown_appcontext(close_db)
    app.cli.add_command(init_db_command)

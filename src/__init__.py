import os

from flask import Flask
from flask import render_template
from flask import request


def create_app(test_config=None):
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_object("config.DevelopmentConfig")

    if test_config is not None:
        app.config.from_object("config.TestingConfig")

    try:
        os.makedirs(app.instance_path)
    except FileExistsError:
        pass
    except OSError as e:
        print("Instance folder doesn't exists and couldn't be created: {}".format(e))


    from . import db
    db.init_app(app)


    @app.route('/', methods=["GET", "POST"])
    def index():
        if request.method == "GET":
            return render_template("index.html")
        elif request.method == "POST":
            artwork = request.form["artwork"].strip().lower()
            db_conn = db.get_db()
            cur = db_conn.cursor()
            cur.execute(
                """SELECT animal_crossing_name, real_life_name, real_life_author, authenticity_helper_info, polygon_image_url
                   FROM artwork
                   WHERE LOWER(animal_crossing_name) LIKE %s
                   LIMIT 1""",
                   ("%{}%".format(artwork),)
            )
            query_result = cur.fetchone()
            if query_result is not None:
                return render_template(
                    "index.html",
                    not_found=False,
                    animal_crossing_name=query_result[0],
                    real_life_name=query_result[1],
                    real_life_author=query_result[2],
                    authenticity_helper_info=query_result[3],
                    polygon_image_url=query_result[4]
                )
            else:
                return render_template("index.html", not_found=True)


    return app


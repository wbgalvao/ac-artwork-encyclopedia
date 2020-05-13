# Animal Crossing Artwork Encyclopedia :fox_face:

## Context
[Animal Crossing: New Horizons](https://animal-crossing.com/new-horizons/) is a Nintendo Switch video game where you basically build a town from a deserted island. One of the first things that you get to build in your island is a museum. During the course of the game you get to donate fishes, bugs, fossils and artwork to this museum. These fishes, bugs and fossils you can find in the island, but the artwork (paintings and statues) you have to buy from a game character called Jolly Redd. The problem is that this character can sell you fake artwork, so you have to be careful.

There is a [Polygon article](https://www.polygon.com/animal-crossing-new-horizons-switch-acnh-guide/2020/4/23/21231433/redd-jolly-museum-art-fake-real-forgeries-list-complete-painting-statue) where you can find a list of artwork with the differences between the real version and the fake version of these artworks. This project is essentially a search engine for the data provided by this article.

## Local Development
This application uses [**Flask**](https://flask.palletsprojects.com/en/1.1.x/) and [**PostgreSQL**](https://www.postgresql.org/). To get a local version running install [Docker](https://www.docker.com/) and [docker-compose](https://docs.docker.com/compose/) and simply run `$ docker-compose up` from project's root directory.

In case you don't want to use Docker, you can also create a virtual environment and install the project's dependencies with `pip`

```shell
$ python -m venv venv
$ source venv/bin/activate
(venv) $ pip install -r requirements.txt
(venv) $ FLASK_APP=src/ FLASK_ENV=development flask run
```

Please note that [psycopg2](https://www.psycopg.org/) have some system dependencies. Check its (installation page)[https://www.psycopg.org/docs/install.html] for more details.

In both cases, after you follow the instructions, the application should be running at localhost port 5000.

## Disclaimer
All data provided by this project was extracted from the previously mentioned Polygon article. All credits for gathering this information goes to it.

## License
[MIT](https://github.com/wbgalvao/ac-artwork-encyclopedia/blob/master/LICENSE)

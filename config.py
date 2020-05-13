class Config(object):
    DEBUG = False
    TESTING = False
    DATABASE_CONNECTION_URI = ""
    DATASOURCE_URL = "https://www.polygon.com/animal-crossing-new-horizons-switch-acnh-guide/2020/4/23/21231433/redd-jolly-museum-art-fake-real-forgeries-list-complete-painting-statue"


class ProductionConfig(Config):
    pass


class DevelopmentConfig(Config):
    DEBUG = True
    SECRET_KEY = "dev"
    DATABASE_CONNECTION_URI = "postgresql://jolly_redd:shady_business@localhost:5432/ac_artwork_encyclopedia"


class TestingConfig(Config):
    TESTING = True
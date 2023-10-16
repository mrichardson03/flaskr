import os

BASEDIR = os.path.abspath(os.path.dirname(__file__))


class Config(object):
    FLASK_ENV = "development"
    DEBUG = False
    TESTING = False
    SECRET_KEY = os.getenv("SECRET_KEY", default="BAD_SECRET_KEY")
    SQLALCHEMY_DATABASE_URI = os.getenv(
        "DATABASE_URI",
        default=f"sqlite:///{os.path.join(BASEDIR, 'instance', 'flaskr.db')}",
    )


class TestingConfig(Config):
    TESTING = True
    SQLALCHEMY_DATABASE_URI = os.getenv(
        "DATABASE_URI",
        default=f"sqlite:///{os.path.join(BASEDIR, 'instance', 'test.db')}",
    )


class ProductionConfig(Config):
    FLASK_ENV = "production"

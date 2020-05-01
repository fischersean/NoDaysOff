from os import environ


class Config:
    """Flask configuration"""

    DEBUG = True

    SECRET_KEY = environ.get("SECRET_KEY")
    FLASK_APP = environ.get("FLASK_APP")
    FLASK_ENV = environ.get("FLASK_ENV")

    SESSION_TYPE = environ.get("SESSION_TYPE")

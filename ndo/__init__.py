import os
from flask import Flask


def create_app():

    # create and configure the app
    app = Flask(__name__, instance_relative_config=False)

    # app.static_url_path = app.config.get("STATIC_FOLDER")
    # # set the absolute path to the static folder
    # app.static_folder = app.root_path + app.static_url_path

    app.config.from_object("config.Config")

    with app.app_context():
        from . import routes

    return app

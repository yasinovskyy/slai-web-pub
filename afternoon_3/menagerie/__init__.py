#!/usr/bin/env python3

from flask import Flask
from menagerie.data_exploration import read_csv_file


def create_app():
    app = Flask(__name__)
    app.config["data"] = read_csv_file("menagerie/data/menagerie.csv")
    from menagerie.routes import main

    app.register_blueprint(main)

    return app

#!/usr/bin/env python3
"""
Flask app initialization

@authors: Roman Yasinovskyy
@version: 2024.7
"""

import pathlib

from flask import Flask
from crud import create


def init_db():
    create.callback("menagerie", "menagerie.csv")


def create_app():
    app = Flask(__name__)
    if not pathlib.Path("menagerie.sqlite3").exists():
        init_db()
    from zoo.routes import main

    app.register_blueprint(main)

    return app

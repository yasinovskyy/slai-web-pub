#!/usr/bin/env python3
"""
Simple menagerie initialization

@author: Roman Yasinovskyy
@version: 2026.7
"""

import pathlib

import dotenv
from flask import Flask


def create_app():
    from menagerie_simple.auth import auth
    from menagerie_simple.crud import init_db, populate_db, read_db
    from menagerie_simple.routes import main

    app = Flask(__name__)
    dotenv.load_dotenv(".flaskenv")
    app.config.from_prefixed_env()
    app.config["DATA_PATH"] = "menagerie_simple/data"
    app.config["DATABASE"] = f"{app.config['DATA_PATH']}/{app.config['DB_NAME']}.db"

    if not pathlib.Path(f"{app.config['DATA_PATH']}/{app.config['DB_NAME']}.db").exists():
        init_db(app.config["DATA_PATH"], f"{app.config['DB_NAME']}.db")
        populate_db(
            app.config["DATA_PATH"], f"{app.config['DB_NAME']}.db", "animal", "menagerie.csv"
        )
    app.data = read_db(app.config["DATA_PATH"], f"{app.config['DB_NAME']}.db", "animal")
    app.register_blueprint(main)
    app.register_blueprint(auth)

    return app

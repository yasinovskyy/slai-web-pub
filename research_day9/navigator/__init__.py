#!/usr/bin/env python3
"""
College navigator app initialization

@authors: Roman Yasinovskyy
@version: 2025.7
"""

import csv
import pathlib
import sqlite3

import dotenv
from flask import Flask
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase

login_manager = LoginManager()
login_manager.login_view = "auth.login"


class Base(DeclarativeBase):
    pass


db = SQLAlchemy(model_class=Base)


def create_app():
    from navigator.auth import auth
    from navigator.routes import main

    app = Flask(__name__)
    dotenv.load_dotenv(".flaskenv")
    app.config.from_prefixed_env()
    app.config["SQLALCHEMY_DATABASE_URI"] = f"sqlite:///{app.config.get('DB_NAME')}.sqlite3"
    login_manager.init_app(app)
    db.init_app(app)
    if not pathlib.Path(app.config.get("SQLALCHEMY_DATABASE_URI")).exists():
        with app.app_context():
            db.create_all()
        with sqlite3.connect(f"instance/{app.config.get('DB_NAME')}.sqlite3") as connection:
            cursor = connection.cursor()
            with open(f"{app.config.get('DB_NAME')}.csv") as data_file:
                data = csv.DictReader(data_file)
                try:
                    cursor.executemany(
                        "INSERT INTO college VALUES(?, ?, ?);",
                        [tuple(row.values()) for row in data],
                    )
                except sqlite3.IntegrityError:
                    pass

    with sqlite3.connect(f"instance/{app.config.get('DB_NAME')}.sqlite3") as connection:
        connection.row_factory = sqlite3.Row
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM college ORDER BY name;")
    app.data = cursor.fetchall()
    app.register_blueprint(main)
    app.register_blueprint(auth)
    return app

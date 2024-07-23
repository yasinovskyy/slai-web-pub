#!/usr/bin/env python3
"""
College navigator app initialization

@authors: Roman Yasinovskyy
@version: 2024.7
"""

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
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///users.db"
    login_manager.init_app(app)
    db.init_app(app)
    if not pathlib.Path(app.config.get("SQLALCHEMY_DATABASE_URI")).exists():
        with app.app_context():
            db.create_all()
    with sqlite3.connect(f"{app.config.get('DB_NAME')}") as connection:
        connection.row_factory = sqlite3.Row
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM college ORDER BY name;")
    app.data = cursor.fetchall()
    app.register_blueprint(main)
    app.register_blueprint(auth)
    return app

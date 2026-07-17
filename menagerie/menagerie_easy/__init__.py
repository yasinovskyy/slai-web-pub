#!/usr/bin/env python3
"""
Menagerie app initialization

@author: Roman Yasinovskyy
@version: 2026.7
"""

import csv
import pathlib

import dotenv
from flask import Flask
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import DeclarativeBase

login_manager = LoginManager()
login_manager.login_view = "auth.login"


class Base(DeclarativeBase):
    pass


db = SQLAlchemy(model_class=Base)


def create_app():
    from menagerie_easy.auth import auth
    from menagerie_easy.models import Animal
    from menagerie_easy.routes import main

    app = Flask(__name__)
    dotenv.load_dotenv(".flaskenv")
    app.config.from_prefixed_env()
    app.config["SQLALCHEMY_DATABASE_URI"] = f"sqlite:///{app.config.get('DB_NAME')}.sqlite3"
    login_manager.init_app(app)
    db.init_app(app)
    if not pathlib.Path(app.config.get("SQLALCHEMY_DATABASE_URI", "")).exists():
        with app.app_context():
            db.create_all()
            with open(f"{app.config.get('DB_NAME')}.csv", "r", encoding="utf-8") as f:
                data = csv.DictReader(f)
                db.session.add_all(
                    [
                        Animal(
                            id=int(animal["id"]),
                            name=animal["name"],
                            age=int(animal["age"]),
                            species=animal["species"],
                            location=animal["location"],
                        )
                        for animal in data
                    ]
                )
                try:
                    db.session.commit()
                except IntegrityError:
                    # db.session.rollback()
                    pass
    with app.app_context():
        app.data = db.session.query(Animal).all()
    app.register_blueprint(main)
    app.register_blueprint(auth)

    return app

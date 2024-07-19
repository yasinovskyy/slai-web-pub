#!/usr/bin/env python3
"""
Menagerie API

@authors: Roman Yasinovskyy
@version: 2024.7
"""

import sqlite3
import dotenv
from flask import Flask
# from flask_cors import CORS


def create_app():
    app = Flask(__name__)
    # CORS(app)
    dotenv.load_dotenv(".flaskenv")
    app.config.from_prefixed_env()
    with sqlite3.connect(f"{app.config.get('DB_NAME')}") as connection:
        connection.row_factory = sqlite3.Row
        cur = connection.cursor()
        cur.execute("SELECT DISTINCT location FROM animal ORDER BY location;")
    app.select_options = [item["location"] for item in cur.fetchall()]
    from menagerie.routes import main

    app.register_blueprint(main)

    return app

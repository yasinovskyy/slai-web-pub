#!/usr/bin/env python3
"""
Menagerie routes

@authors: Roman Yasinovskyy
@version: 2024.7
"""

from functools import cache
import sqlite3
from flask import Blueprint, current_app, render_template
from flask_cors import cross_origin

main = Blueprint("main", __name__, url_prefix="/")


@main.route("/")
def index():
    return render_template("index.html", options=current_app.select_options)


@main.get("/api/v1/location/<string:location>")
@cross_origin()
@cache
def location_api(location: str):
    with sqlite3.connect(f"{current_app.config.get('DB_NAME')}") as connection:
        connection.row_factory = sqlite3.Row
        cur = connection.cursor()
        cur.execute("SELECT * FROM animal WHERE location=?;", (location,))
    return {"data": [tuple(record) for record in cur.fetchall()]}

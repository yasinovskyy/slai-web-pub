#!/usr/bin/env python3
"""
Flask app routes

@authors: Roman Yasinovskyy
@version: 2024.7
"""

from flask import Blueprint, render_template
from crud import read

main = Blueprint("main", __name__, url_prefix="/")


@main.get("/")
def get_index():
    data = read.callback("menagerie", "animal")
    return render_template("index.jinja", data=data)

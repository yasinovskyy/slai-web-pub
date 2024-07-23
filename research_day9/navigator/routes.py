#!/usr/bin/env python3
"""
College navigator routes

@authors: Roman Yasinovskyy
@version: 2024.7
"""

from flask import Blueprint, current_app, render_template
from flask_login import login_required

main = Blueprint("main", __name__, url_prefix="/")


@main.route("/")
def index():
    return render_template("index.html", data=current_app.data)


@main.get("/profile")
@login_required
def profile():
    return render_template("index.html")

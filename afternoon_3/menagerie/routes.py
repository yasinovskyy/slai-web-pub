#!/usr/bin/env python3

from flask import Blueprint, current_app, render_template, send_from_directory

from menagerie.logic import find_by_id

main = Blueprint("main", __name__, url_prefix="/")


@main.route("/")
def home():
    return render_template("home.jinja", menagerie=current_app.config["data"])


@main.route("/<int:animal_id>")
def details(animal_id: int):
    the_animal = find_by_id(animal_id)
    if the_animal:
        return render_template("details.jinja", animal=the_animal)
    return "Information on this animal has not been found"

#!/usr/bin/env python3

from pokesearch.logic import query
from flask import Blueprint, abort, current_app, render_template, request


main = Blueprint("main", __name__, url_prefix="/")


@main.get("/")
def index():
    return render_template("poke_form.html", types=current_app.poke_types)


@main.post("/search")
def post_index():
    return render_template("index.html", data=query(dict(request.form)))


@main.route("/<int:pokemon_id>")
def pok_by_id(pokemon_id: int):
    data = [record for record in current_app.data if int(record["ID"]) == pokemon_id]
    if data:
        return render_template("details.html", data=data)
    abort(404)


@main.route("/<string:pokemon_name>")
def pok_by_name(pokemon_name: str):
    data = [record for record in current_app.data if record["Name"] == pokemon_name]
    if data:
        return render_template("details.html", data=data[0])
    abort(404)


@main.errorhandler(404)
def not_found(error):
    return "No pokemon here"

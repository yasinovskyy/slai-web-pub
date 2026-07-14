from flask import Blueprint, current_app, send_from_directory, render_template, request
import random
from pookiedex.logic import query
from pookiedex.crud import read_db, query_db

main = Blueprint("main", __name__, url_prefix="/")


@main.route("/")
def home():
    return render_template(
        "home.jinja",
        poke_id=random.randint(1, 1025),
        data=read_db("pookiedex/data/pookiedex.db", "allpokemon"),
    )


@main.route("/about")
def about():
    return send_from_directory("static", "about.html")


@main.get("/search")
def search():
    return render_template(
        "search.jinja",
        message="Use the search form",
        poke_id=1025,
        primary_typing=current_app.config["primary_types"],
        secondary_typing=current_app.config["secondary_types"],
        generations=current_app.config["generation"],
    )


@main.post("/search")
def search_results():
    result = query(request.form)
    return render_template("home.jinja", poke_id=8, data=result)


@main.route("/<int:poke_id>")
def pokemon_by_id(poke_id: int):
    data = query_db(
        "pookiedex/data/pookiedex.db",
        "select * from allpokemon where `National Dex #`=?;",
        poke_id,
    )
    if data:
        result = "<br>".join(
            [f"Pokemon #{poke_id} is {pokemon['Name'].capitalize()}" for pokemon in data]
        )
        return result
    return f"Information on pokemon #{poke_id} is under construction"


@main.route("/<string:poke_name>")
def pokemon_by_name(poke_name: str):
    data = query_db(
        "pookiedex/data/pookiedex.db",
        "select * from allpokemon where Name=?;",
        poke_name,
    )
    for pokemon in data:
        return f"Pokemon {poke_name} is {pokemon['Primary Typing'].capitalize()}"
    return f"Information on pokemon {poke_name} is under construction"

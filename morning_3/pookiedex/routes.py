from flask import Blueprint, current_app, send_from_directory, render_template, request
import random
from pookiedex.logic import query

main = Blueprint("main", __name__, url_prefix="/")


@main.route("/")
def home():
    return render_template(
        "home.jinja", poke_id=random.randint(1, 1025), data=current_app.config["data"]
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
        primary_typing=["water", "fire", "bug"],
        secondary_typing=["poison", "dragon", "flying"],
        generations=["i", "ii", "iii", "iv", "v", "vi", "vii", "viii", "ix"],
    )


@main.post("/search")
def search_results():
    result = query(request.form)
    return render_template("home.jinja", poke_id=8, data=result)


@main.route("/<int:poke_id>")
def pokemon_by_id(poke_id: int):
    for pokemon in current_app.config["data"]:
        if int(pokemon["National Dex #"]) == poke_id:
            return f"Pokemon #{poke_id} is {pokemon['Name'].capitalize()}"
    return f"Information on pokemon #{poke_id} is under construction"


@main.route("/<string:poke_name>")
def pokemon_by_name(poke_name: str):
    for pokemon in current_app.config["data"]:
        if pokemon["Name"] == poke_name:
            return f"Pokemon {poke_name} is {pokemon['Primary Typing'].capitalize()}"
    return f"Information on pokemon {poke_name} is under construction"

from flask import Flask, send_from_directory, render_template
from data_exploration import read_csv_file
import random


def create_app():
    app = Flask(__name__)
    app.config["data"] = read_csv_file("pokemon.csv")
    app.config["poke_id"] = random.randint(1, 1025)
    return app


app = create_app()


@app.route("/")
def home():
    return render_template("home.jinja", poke_id=random.randint(1, 1025), data=app.config["data"])


@app.route("/about")
def about():
    return send_from_directory("static", "about.html")


@app.route("/search")
def search():
    return render_template("home.jinja", message="Under construction", poke_id=1025)


@app.route("/<int:poke_id>")
def pokemon_by_id(poke_id: int):
    data = read_csv_file("pokemon.csv")
    for pokemon in data:
        if int(pokemon["National Dex #"]) == poke_id:
            return f"Pokemon #{poke_id} is {pokemon['Name'].capitalize()}"
    return f"Information on pokemon #{poke_id} is under construction"


@app.route("/<string:poke_name>")
def pokemon_by_name(poke_name: str):
    data = read_csv_file("pokemon.csv")
    for pokemon in data:
        if pokemon["Name"] == poke_name:
            return f"Pokemon {poke_name} is {pokemon['Primary Typing'].capitalize()}"
    return f"Information on pokemon {poke_name} is under construction"

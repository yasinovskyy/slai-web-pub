from flask import Flask
from data_exploration import read_csv_file

app = Flask(__name__)


@app.route("/")
def home():
    return "Welcome to OUR Homepage!!!!"


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

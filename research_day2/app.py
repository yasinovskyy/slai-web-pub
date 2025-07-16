#!/usr/bin/env python3

from data_exploration import read_csv
from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def index():
    data = read_csv("pokemon.csv")
    return render_template("index.html", data=data)


@app.route("/<int:pokemon_num>")
def pok_details(pokemon_num: int):
    data = [record for record in read_csv("pokemon.csv") if int(record["#"]) == pokemon_num]
    return data


@app.route("/<string:pokemon_name>")
def pok_by_name(pokemon_name: str):
    data = [record for record in read_csv("pokemon.csv") if record["Name"] == pokemon_name]
    return render_template("details.html", data=data[0])

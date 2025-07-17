#!/usr/bin/env python3

from data_exploration import read_csv
from flask import Flask, render_template, request

app = Flask(__name__)


@app.get("/")
def index():
    poke_types = set()
    data = read_csv("pokemon.csv")
    for record in data:
        poke_types.add(record["Type 1"])
    return render_template("poke_form.html", types=sorted(poke_types))


@app.post("/search")
def post_index():
    return render_template("index.html", data=query(dict(request.form)))


@app.route("/<int:pokemon_id>")
def pok_by_id(pokemon_id: int):
    data = [record for record in read_csv("pokemon.csv") if int(record["ID"]) == pokemon_id]
    return data


@app.route("/<string:pokemon_name>")
def pok_by_name(pokemon_name: str):
    data = [record for record in read_csv("pokemon.csv") if record["Name"] == pokemon_name]
    return render_template("details.html", data=data[0])


def query(form: dict):
    result = []
    data = read_csv("pokemon.csv")
    for record in data:
        if (
            form["primary_type"] == record["Type 1"] or form["primary_type"] == record["Type 2"]
        ) and int(form["min_health"]) <= record["HP"] <= int(form["max_health"]):
            result.append(record)

    return result

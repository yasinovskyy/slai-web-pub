#!/usr/bin/env python3

from data_exploration import read_csv
from flask import Flask

app = Flask(__name__)


@app.route("/")
def index():
    return "<strong>Hello, sleepy students</strong>"


@app.route("/<int:pokemon_num>")
def pok_details(pokemon_num: int):
    data = read_csv("pokemon.csv")
    for mon in data:
        if int(mon["#"]) == pokemon_num:
            return mon
    return "No monsters here!"

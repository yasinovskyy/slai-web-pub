#!/usr/bin/env python3

from string import Template
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
            detailed_data = {
                "name": mon["Name"],
                "gen": mon["Generation"],
                "type": mon["Type 1"] + " " + mon["Type 2"],
            }
            with open("details.txt", "r", encoding="utf-8") as t_file:
                template = Template(t_file.read())
                return template.substitute(detailed_data)
    return "No monsters here!"


@app.route("/attack/<int:min_val>/<int:max_val>")
def pok_by_attack(min_val: int, max_val: int): ...


@app.route("/defense/<int:min_val>/<int:max_val>")
def pok_by_defense(min_val: int, max_val: int): ...


@app.route("/legendary")
def pok_by_status(): ...

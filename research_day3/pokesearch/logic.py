#!/usr/bin/env python

import csv
from flask import current_app


def read_csv(filename: str):
    result = []
    with open(filename) as f:
        for item in csv.DictReader(f):
            result.append(
                {
                    "ID": int(item["#"]),
                    "Name": item["Name"],
                    "Type 1": item["Type 1"],
                    "Type 2": item["Type 2"],
                    "Total": int(item["Total"]),
                    "HP": int(item["HP"]),
                    "Attack": int(item["Attack"]),
                    "Defense": int(item["Defense"]),
                    "Special Attack": int(item["Sp. Atk"]),
                    "Special Defense": int(item["Sp. Def"]),
                    "Speed": int(item["Speed"]),
                    "Generation": int(item["Generation"]),
                    "Legendary": item["Legendary"] == "True",
                }
            )
    return result


def query(form: dict):
    result = []
    for record in current_app.data:
        if (
            form["primary_type"] == record["Type 1"] or form["primary_type"] == record["Type 2"]
        ) and int(form["min_health"]) <= record["HP"] <= int(form["max_health"]):
            result.append(record)

    return result

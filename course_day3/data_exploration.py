#!/usr/bin/env python

import csv


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
                    "Legendary": True if item["Legendary"] == "True" else False,
                }
            )
    return result

#!/usr/bin/env python3

from flask import current_app


def query(form: dict):
    result = []

    return result


def find_by_id(animal_id: int):
    for animal in current_app.config["data"]:
        if int(animal["id"]) == animal_id:
            return animal

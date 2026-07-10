#!/usr/bin/env python3
"""
Serving `pyjokes` via templates
Application initialization

@author: Roman Yasinovskyy
@version: 2026.7
"""

from flask import Flask


def create_app():
    app = Flask(__name__)
    app.config["numbers"] = range(1, 10)
    app.config["languages"] = {
        "en": "ENGLISH",
        "cs": "CZECH",
        "de": "GERMAN",
        "es": "SPANISH",
        "eu": "BASQUE",
        "fr": "FRENCH",
        "gl": "GALICIAN",
        "hu": "HUNGARIAN",
        "it": "ITALIAN",
        "lt": "LITHUANIAN",
        "pl": "POLISH",
        "sv": "SWEDISH",
    }
    app.config["categories"] = {
        "all": "All",
        "chuck": "Chuck Norris",
        "neutral": "Neutral",
    }
    from joker.routes import main

    app.register_blueprint(main)
    return app

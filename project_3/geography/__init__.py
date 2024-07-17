#!/usr/bin/env python3
"""
Regions of the world

@authors: Roman Yasinovskyy
@version: 2024.7
"""

import dotenv
from flask import Flask

from geography.logic import read_db


def create_app():
    app = Flask(__name__)
    dotenv.load_dotenv(".flaskenv")
    app.config.from_prefixed_env()
    ...
    # TODO: Countries to use in the `dl_countries`
    app.countries = []
    # TODO: Regions to use in the `select_region`
    app.regions = []
    # TODO: Continents to use in the `select_continent`
    app.continents = []
    from geography.routes import main

    app.register_blueprint(main)
    return app

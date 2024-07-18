#!/usr/bin/env python3
"""
Flask app initialization

@authors: Roman Yasinovskyy
@version: 2024.7
"""

from flask import Flask


def create_app():
    app = Flask(__name__)
    from trivia.routes import main

    app.register_blueprint(main)

    return app

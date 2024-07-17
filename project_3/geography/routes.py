#!/usr/bin/env python3
"""
Geography query app

@authors: Roman Yasinovskyy
@version: 2024.7
"""

from flask import (
    Blueprint,
    abort,
    current_app,
    flash,
    render_template,
    request,
)

from geography.logic import read_db

main = Blueprint("main", __name__, url_prefix="/")


@main.get("/")
def get_index() -> str:
    """Display selection form"""
    return render_template("index.html")


@main.post("/")
def post_index() -> str:
    """Handle selection

    Build a query based on the form and supply this query to `logic.read_db`
    """
    # TODO: Implement this function
    ...
    result = []

    return render_template(
        "index.html",
        data=result,
    )


@main.errorhandler(404)
def not_found(error):
    return render_template("index.html", error=error), 404


@main.context_processor
def add_select_options():
    return {
        "countries": current_app.countries,
        "regions": current_app.regions,
        "continents": current_app.continents,
    }

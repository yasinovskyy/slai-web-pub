#!/usr/bin/env python3
"""
Serving `pyjokes` via templates
Application routes

@author:
@version: 2026.7
"""

from flask import Blueprint, current_app, render_template, request

from joker.logic import query

main = Blueprint("main", __name__, url_prefix="/")


@main.get("/")
def show_form():
    """Render the template with form"""
    # TODO: Implement this function
    ...


@main.post("/")
def process_form():
    """Render the template with jokes"""
    # TODO: Implement this function
    ...

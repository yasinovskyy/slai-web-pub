#!/usr/bin/env python3
"""Interacting with the database"""

import pathlib
import sqlite3


def read_db(query: str, args: tuple = tuple()) -> list:
    """Retrieve data from the database

    :param query: query to execute
    """
    with sqlite3.connect(pathlib.Path("geography/data/world.sqlite3")) as sqlite3_conn:
        sqlite3_conn.row_factory = sqlite3.Row
        return sqlite3_conn.cursor().execute(query, args).fetchall()

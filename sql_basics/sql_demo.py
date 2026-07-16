#!/usr/bin/env python3
"""Working with databases"""

import sqlite3


def query_db(db_name: str, query: str):
    """Query the database"""
    with sqlite3.connect(f"{db_name}") as connection:
        connection.row_factory = sqlite3.Row
        cursor = connection.cursor()
        cursor.execute(query)
    return cursor.fetchall()


def main():
    """Main function"""
    result = query_db("chinook.db", "SELECT * FROM invoices")
    for record in result:
        print(dict(record))


if __name__ == "__main__":
    main()

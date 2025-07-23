#!/usr/bin/env python3
"""Working with records"""

import sqlite3


def read_natively(db_name: str, table: str) -> None:
    """Read all records"""
    with sqlite3.connect(f"{db_name}") as connection:
        # connection.row_factory = sqlite3.Row
        cursor = connection.cursor()
        cursor.execute(f"SELECT * FROM {table} limit 10;")
        for record in cursor:
            print(record)


def main():
    """Main function"""
    read_natively("chinook.db", "artists")


if __name__ == "__main__":
    main()

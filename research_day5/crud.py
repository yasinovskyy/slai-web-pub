#!/usr/bin/env python3
"""Working with SQLite3"""

import csv
from functools import cache
import logging
import sqlite3
from typing import Any

import click


@click.command(help="Create a database from the CSV file")
@click.argument("db_name")
@click.option("--datafile", default="menagerie.csv")
def create(db_name: str, datafile: str) -> None:
    """Create database"""
    print("CREATE")
    with sqlite3.connect(f"{db_name}.sqlite3") as connection:
        with open(datafile, "r") as input_file:
            data = csv.DictReader(input_file)
            cur = connection.cursor()
            cur.execute("DROP TABLE IF EXISTS animal;")
            cur.execute(
                "CREATE table animal ("
                + "id integer primary key,"
                + "name,"
                + "age integer,"
                + "species,"
                + "location"
                + ");"
            )
            cur.executemany(
                "INSERT INTO animal values(?, ?, ?, ?, ?);", (tuple(ani.values()) for ani in data)
            )


@click.command(help="Read all records from the specified table")
@click.argument("db_name")
@click.option("--table", "-t", default="animal")
@cache
def read(db_name: str, table: str) -> None | list[Any]:
    """Read all records"""
    print("READ")
    with sqlite3.connect(f"{db_name}.sqlite3") as connection:
        connection.row_factory = sqlite3.Row
        cur = connection.cursor()
        cur.execute(f"SELECT * FROM {table};")
    return cur.fetchall()


@click.command()
@click.argument("db_name")
@click.option("--table", "-t", default="animal")
@click.option("--location", "-l", default="", help="Location to read")
@click.option("--species", "-s", default="", help="Species to read")
def query(db_name: str, table: str, species: str, location: str) -> None:
    """Query records"""
    print("QUERY")


@click.command()
@click.argument("db_name")
@click.option("--table", "-t", default="animal")
@click.option("--animal", "-a", help="Animal to update", type=int, default=0)
def update(db_name: str, table: str, animal: int) -> None:
    """Update records"""
    print("UPDATE")


@click.command()
@click.argument("db_name")
@click.option("--table", "-t", default="animal")
@click.option("--animal", "-a", help="Animal to update", type=int, default=0)
@click.option("--species", "-s", default="", help="Species to delete")
def delete(db_name: str, table: str, animal: int, species: str) -> None:
    """Delete records"""
    print("DELETE")


@click.group()
@click.option("--verbose", "-v", is_flag=True, default=False)
def cli(verbose: bool):
    """Command-line interface"""
    if verbose:
        logging.basicConfig(level=logging.INFO)


def main():
    """Main function"""
    cli.add_command(create)
    cli.add_command(read)
    cli.add_command(query)
    cli.add_command(update)
    cli.add_command(delete)
    cli()


if __name__ == "__main__":
    main()

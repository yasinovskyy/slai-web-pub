#!/usr/bin/env python

import csv
import sqlite3


def read_csv(filename: str):
    """Read data from a csv file as a list of dictionaries

    :param filename: name of the data source file
    """
    with open(filename) as f:
        return list(csv.DictReader(f))


def init_db(path: str, db_name: str):
    """Initialize the database

    :param path: path to the database file
    :param db_name: name of the database
    """
    with sqlite3.connect(f"{path}/{db_name}") as connection:
        cursor = connection.cursor()
        cursor.execute(
            """
CREATE TABLE IF NOT EXISTS user(
"id" INTEGER PRIMARY KEY AUTOINCREMENT,
"name" TEXT,
"email" TEXT UNIQUE,
"password" TEXT
);
"""
        )
        cursor.execute(
            """
CREATE TABLE IF NOT EXISTS animal(
"id" INTEGER PRIMARY KEY NOT NULL,
"name" TEXT,
"age" INTEGER,
"species" TEXT,
"location" TEXT
);
"""
        )
        cursor.execute(
            """
CREATE TABLE IF NOT EXISTS adoption(
"id" INTEGER PRIMARY KEY NOT NULL,
"user_id" INTEGER,
"animal_id" INTEGER,
FOREIGN KEY(user_id) REFERENCES user(id),
FOREIGN KEY(animal_id) REFERENCES animal(id)
);
"""
        )


def populate_db(path: str, db_name: str, table: str, data_file: str):
    """Add data from a csv file to the specific table

    :param path: path to the database file
    :param db_name: name of the database
    :param table: table to use
    :param data_file: source data file
    """
    with sqlite3.connect(f"{path}/{db_name}") as connection:
        with open(f"{data_file}") as f:
            data = csv.DictReader(f)
            cursor = connection.cursor()
            cursor.executemany(
                f"INSERT INTO {table} VALUES(?, ?, ?, ?, ?);",
                (tuple(p.values()) for p in data),
            )


def add_user(path: str, db_name: str, user: dict):
    """Add a new user

    :param path: path to the database file
    :param db_name: name of the database
    :param user: user properties
    """
    with sqlite3.connect(f"{path}/{db_name}") as connection:
        cursor = connection.cursor()
        cursor.execute(
            "INSERT INTO user(name, email, password) VALUES(?, ?, ?);",
            tuple(user.values()),
        )


def add_adoption(path: str, db_name: str, user_id: int, animal_id: int):
    """Add a new animal adoption

    :param path: path to the database file
    :param db_name: name of the database
    :param user_id: user id
    :param animal_id: animal id
    """
    with sqlite3.connect(f"{path}/{db_name}") as connection:
        cursor = connection.cursor()
        cursor.execute(
            "INSERT INTO adoption(user_id, animal_id) VALUES(?, ?);",
            (user_id, animal_id),
        )


def remove_adoption(path: str, db_name: str, user_id: int, animal_id: int):
    """FRemove an animal adoption

    :param path: path to the database file
    :param db_name: name of the database
    :param user_id: user id
    :param animal_id: animal id
    """
    with sqlite3.connect(f"{path}/{db_name}") as connection:
        cursor = connection.cursor()
        cursor.execute(
            "DELETE FROM adoption WHERE user_id=? and animal_id=?;",
            (user_id, animal_id),
        )


def update_user(path: str, db_name: str, user_id: int, new_name: str, new_password: str):
    """Update user password

    :param path: path to the database file
    :param db_name: name of the database
    :param user_id: id of the user
    :param new_name: the new n ame
    :param new_password: (hash of) the new password
    """
    with sqlite3.connect(f"{path}/{db_name}") as connection:
        cursor = connection.cursor()
        cursor.execute(
            f"UPDATE user SET name=?, password=? WHERE id={user_id} ;",
            (new_name, new_password),
        )


def retrieve_by_id(path: str, db_name: str, table: str, record_id: int):
    """Retrieve a record by its id

    :param path: path to the database file
    :param db_name: name of the database
    :param table: table to use
    :param record_id: id of the record
    """
    with sqlite3.connect(f"{path}/{db_name}") as connection:
        cursor = connection.cursor()
        cursor.execute(
            f"SELECT * FROM {table} WHERE id={record_id}",
        )
    return cursor.fetchone()


def read_db(path: str, db_name: str, table: str):
    """Read all records from a single table

    :param path: path to the database file
    :param db_name: name of the database
    :param table: table to use
    """
    with sqlite3.connect(f"{path}/{db_name}") as connection:
        connection.row_factory = sqlite3.Row
        cursor = connection.cursor()
        cursor.execute(f"SELECT * FROM {table};")
    return cursor.fetchall()


def query_db(path: str, db_name: str, query: str, params=None, firstone=False):
    """Run a custom query on a specific table

    :param path: path to the database file
    :param db_name: name of the database
    :param query: parametrized SQL query
    :param params: optional parameters
    """
    with sqlite3.connect(f"{path}/{db_name}") as connection:
        connection.row_factory = sqlite3.Row
        cursor = connection.cursor()
        if params:
            cursor.execute(query, params)
        else:
            cursor.execute(query)
    if firstone:
        return cursor.fetchone()
    return cursor.fetchall()


if __name__ == "__main__":
    ...
    # init_db(".", "menagerie-test.db")
    # populate_db(".", "menagerie-test.db", "animal", "../menagerie.csv")
    add_user(
        ".",
        "menagerie-test.db",
        {"name": "Alice", "email": "alice@example.com", "password": "hash"},
    )
    # print(retrieve_by_id(".", "menagerie-test.db", "animal", 2))
    # print(retrieve_by_id(".", "menagerie-test.db", "user", 1))
    # print(
    #     [
    #         dict(a)
    #         for a in query_db(
    #             ".", "menagerie-test.db", "SELECT * FROM animal WHERE location=?", "Attic"
    #         )
    #     ]
    # )

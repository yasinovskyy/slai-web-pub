import sqlite3
from pookiedex.data_exploration import read_csv_file


def init_db(db_name: str, table: str):
    statement = f"""
CREATE TABLE IF NOT EXISTS "{table}"(
"Name" TEXT, "National Dex #" INTEGER, "Primary Typing" TEXT, "Secondary Typing" TEXT,
 "Secondary Typing Flag" TEXT, "Generation" TEXT, "Legendary Status" TEXT, "Form" TEXT,
 "Alt Form Flag" TEXT, "Evolution Stage" INTEGER, "Number of Evolution" INTEGER, "Color ID" TEXT,
 "Catch Rate" INTEGER, "Height (dm)" INTEGER, "Weight (hg)" INTEGER, "Height (in)" INTEGER,
 "Weight (lbs)" INTEGER, "Base Stat Total" INTEGER, "Health" INTEGER, "Attack" INTEGER,
 "Defense" INTEGER, "Special Attack" INTEGER, "Special Defense" INTEGER, "Speed" INTEGER);
"""
    with sqlite3.connect(db_name) as conn:
        cur = conn.cursor()
        cur.execute(statement)


def populate_db(db_name: str, table: str, datafile: str):
    data = read_csv_file(datafile)
    print(f"****Populating with {len(data)} records****")
    with sqlite3.connect(db_name) as conn:
        cur = conn.cursor()
        cur.executemany(
            f"insert into {table} values(?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?);",
            (tuple(p.values()) for p in data),
        )


def read_db(db_name: str, table: str):
    with sqlite3.connect(db_name) as conn:
        conn.row_factory = sqlite3.Row
        cur = conn.cursor()
        cur.execute(f"select * from {table};")
    return cur.fetchall()


def query_db(db_name: str, query: str, params=None):
    with sqlite3.connect(db_name) as conn:
        conn.row_factory = sqlite3.Row
        cur = conn.cursor()
        if params is not None:
            cur.execute(query, tuple((params,)))
        else:
            cur.execute(query)
    return cur.fetchall()


# if __name__ == "__main__":
#     init_db("data/pookiedex.db", "allpokemon")
#     populate_db("data/pookiedex.db", "allpokemon", "data/pokemon.csv")
#     print(read_db("data/pookiedex.db", "allpokemon"))

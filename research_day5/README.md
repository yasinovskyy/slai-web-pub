# Day 5. Using databases

Python comes with SQLite built-in but can work with many other Database Management Systems via connectors and adapters.

- SQLite3
- MySQL
- PostgreSQL
- MongoDB

## SQLite3

Built into Python. Simple yet powerful file-based database.

```python
import sqlite3

conn = sqlite3.connect("chinook.db")
cur = conn.cursor()
cur.execute("select * from artists limit 10")
rows = cur.fetchall()
print(rows)
```

## `sqlite3` command-line tool

Create an empty database:

```bash
$ sqlite3 menagerie.sqlite3
```

Switch to the `csv` mode:

```bash
sqlite> .mode csv
```

Import data from a file into a table:

```bash
sqlite> .import menagerie.csv animal
```

Check the database schema:

```sql
sqlite> .schema
CREATE TABLE IF NOT EXISTS "animal"(
"id" TEXT, "name" TEXT, "age" TEXT, "species" TEXT,
 "location" TEXT);
```

Leave the `sqlite3` prompt:

```bash
sqlite> .quit
```

Delete the database file:

```bash
$ rm menagerie.sqlite3
```

Create an empty database:

```bash
$ sqlite3 menagerie.sqlite3
```

Switch to the `csv` mode:

```bash
sqlite> .mode csv
```

Create the table using the previously seen schema with some modifications:

```sql
sqlite> create table 'animal' ('id' integer not null primary key, 'name' text, 'age' integer, 'species' text, 'location' text);
```

Import data from a file into a table:

```bash
sqlite> .import menagerie.csv animal
```

One record (first line) may cause `INSERT failed: datatype mismatch` error but the rest should go through. Delete the first line (csv heading) if necessary.

Check the database schema:

```sql
sqlite> .schema
CREATE TABLE IF NOT EXISTS 'animal' ('id' integer not null primary key, 'name' text, 'age' integer, 'species' text, 'location' text);
```

Alter the database, if necessary:

```sql
sqlite> alter table animal drop column 'species';
```

Leave the `sqlite3` prompt:

```bash
sqlite> .quit
```

## References

- [SQLite Home Page](https://www.sqlite.org/)
- [sqlite3 — DB-API 2.0 interface for SQLite databases — Python 3.12.4 documentation](https://docs.python.org/3/library/sqlite3.html)
- [A Beginner’s Guide to the True Order of SQL Operations – Java, SQL and jOOQ.](https://blog.jooq.org/a-beginners-guide-to-the-true-order-of-sql-operations/)

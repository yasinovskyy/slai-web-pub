# Day 7. SQL

SQL is a powerful data manipulation language.

## `select .. from`

Find all records in the `invoices` table.

```sql
SELECT *
FROM invoices
```

Find countries in the `invoices` table.

```sql
SELECT BillingCountry
FROM invoices
```

## `distinct`

Find different countries in the `invoices` table.

```sql
SELECT DISTINCT BillingCountry
FROM invoices
```

## `limit`

Find 10 different countries in the `invoices` table.

```sql
SELECT DISTINCT BillingCountry
FROM invoices
LIMIT 10
```

## `order by asc|desc`

Find different countries in the `invoices` table and order them by name.

```sql
SELECT DISTINCT BillingCountry
FROM invoices
ORDER BY BillingCountry
```

## `as`

Find different countries in the `invoices` table and rename the field as it appears in the resulting table.

```sql
SELECT DISTINCT BillingCountry AS country
FROM invoices
ORDER BY country
```

## `where`

Only find tracks with a specific composer.

```sql
SELECT Name
FROM tracks
WHERE Composer = "Chuck Berry"
```

## `and|or|not`

Only find tracks with a specific composer _and_ duration.

```sql
SELECT *
FROM tracks
WHERE Composer = "Chuck Berry" AND Milliseconds < 200000
```

## `like`

Only find tracks with a composer's name matching a pattern.

```sql
SELECT *
FROM tracks
WHERE Composer LIKE "%Chuck%"
```

## `is [not] null`

Only find tracks if the composer is not specified.

```sql
SELECT *
FROM tracks
WHERE Composer IS NULL
```

## `in`

Only find invoices with a country from the specific list of options.

```sql
SELECT *
FROM invoices
WHERE BillingCountry IN ("USA", "Norway")
```

## `group by`

Organize records of the `invoices` table into groups based on the country name and find number of invoices in each group.

```sql
SELECT BillingCountry, count(*)
FROM invoices
GROUP BY BillingCountry
```

Aggregate functions

### `count`

```sql
SELECT count(*)
FROM invoices
```

```sql
SELECT BillingCountry, count(*)
FROM invoices
GROUP BY BillingCountry
ORDER BY  count(*)
```

### `min`

```sql
SELECT BillingCountry, min(InvoiceDate) AS first_order
FROM invoices
GROUP BY BillingCountry
ORDER BY first_order
-- ORDER BY BillingCountry
```

### `max`

```sql
SELECT InvoiceDate, max(Total)
FROM invoices
GROUP BY InvoiceDate
ORDER BY  max(Total) DESC
```

### `avg`

```sql
SELECT BillingCountry, round(avg(Total), 2)
FROM invoices
GROUP BY BillingCountry
ORDER BY avg(Total) DESC
```

### `sum`

```sql
SELECT BillingCountry, sum(Total) AS total_sum
FROM invoices
GROUP BY BillingCountry
ORDER BY total_sum DESC
```

## `having`

Use the result of the aggregate function as a filter.

```sql
SELECT BillingCountry, count(*) as orders
FROM invoices
GROUP BY BillingCountry
HAVING orders > 20
ORDER BY orders DESC
```

## `union`

Combine two relations (tables) of the similar structure.

```sql
SELECT *
FROM tracks
WHERE Composer LIKE "%Berry%"
UNION 
SELECT *
FROM tracks
WHERE Composer LIKE "%Perry%"
```

## `product`

Create a cartesian product of multiple tables.

```sql
SELECT *
FROM albums, artists
```

A common pattern is the cartesian product followed by a filter based on equality of two fields.

```sql
SELECT *
FROM albums, artists
WHERE albums.ArtistId=artists.ArtistId
```

## `join`

A (much) more efficient way to filter based on the fields equality.

```sql
SELECT *
FROM albums JOIN artists 
ON albums.ArtistId=artists.ArtistId
```

Not all operations are implemented in all database management systems.

- `inner join .. on` selects records that have matching values in both tables.
- `left join` returns all records from the left table (table1), and the matching records from the right table (table2).
- `full [outer] join` returns all records when there is a match in left (table1) or right (table2) table records.

## More queries

Display floating-point numbers with the specified precision.

```sql
SELECT BillingCountry, printf("$%15.2f", avg(Total), 2) as AverageOrder
FROM invoices
GROUP BY BillingCountry
ORDER BY AverageOrder DESC
```

Find an id of the album with the most tracks.

```sql
SELECT AlbumId, count(Name) AS num_of_tracks
FROM tracks
GROUP BY AlbumId
ORDER BY num_of_tracks DESC
LIMIT 1
```

Find an artist that released an album with the most tracks.

```sql
WITH most_tracks AS (
SELECT AlbumId, count(Name) AS num_of_tracks
FROM tracks
GROUP BY AlbumId
ORDER BY num_of_tracks DESC
LIMIT 1
)
SELECT *
FROM most_tracks 
JOIN albums ON most_tracks.AlbumId=albums.AlbumId 
JOIN artists ON albums.ArtistId=artists.ArtistId
```

Find an artist that released an album with the most tracks.

```sql
SELECT Name
FROM albums JOIN artists ON albums.ArtistId=artists.ArtistId
WHERE AlbumId=(
SELECT AlbumId
FROM tracks
GROUP BY AlbumId
ORDER BY count(Name) DESC
LIMIT 1
)
```

Find an artist with the longest album.

```sql
WITH longest_album AS (
SELECT AlbumId, sum(Milliseconds) AS album_duration
FROM tracks
GROUP BY AlbumId
ORDER BY album_duration DESC
LIMIT 1
)
SELECT *
FROM longest_album 
JOIN albums ON longest_album.AlbumId=albums.AlbumId 
JOIN artists ON albums.ArtistId=artists.ArtistId
```

## References

- [sqlite3 — DB-API 2.0 interface for SQLite databases — Python 3.12.4 documentation](https://docs.python.org/3/library/sqlite3.html)
- [SQLite Sample Database And Its Diagram (in PDF format)](https://www.sqlitetutorial.net/sqlite-sample-database/)
- [SQL Tutorial](https://www.w3schools.com/sql/default.asp)
- [DB Browser for SQLite](https://sqlitebrowser.org/)
- [A Beginner’s Guide to the True Order of SQL Operations – Java, SQL and jOOQ.](https://blog.jooq.org/a-beginners-guide-to-the-true-order-of-sql-operations/)

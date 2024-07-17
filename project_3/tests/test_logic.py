#!/usr/bin/env python3
"""
Using pytest-flask to test the back end

@authors: Roman Yasinovskyy
@version: 2024.7
"""

import pytest
from geography.logic import read_db


@pytest.mark.parametrize(
    "query, results",
    [
        ("select * from country;", 250),
        ("select * from country left join city on country.capital=city.id;", 250),
        ("select * from country join city on country.capital=city.id;", 244),
        ("select * from country where capital is null;", 6),
    ],
)
def test_db_all(query, results):
    """Querying the database"""
    assert len(read_db(query)) == results


@pytest.mark.parametrize(
    "query, args, results",
    [
        ("select distinct subregion from country;", tuple(), 23),
        ("select * from country where subregion is null;", tuple(), 5),
        ("select * from country where subregion=?;", ("Australia and New Zealand",), 5),
        ("select * from country where subregion=?;", ("Caribbean",), 28),
        ("select * from country where subregion=?;", ("Central America",), 7),
        ("select * from country where subregion=?;", ("Central Asia",), 5),
        ("select * from country where subregion=?;", ("Eastern Africa",), 21),
        ("select * from country where subregion=?;", ("Eastern Asia",), 8),
        ("select * from country where subregion=?;", ("Eastern Europe",), 10),
        ("select * from country where subregion=?;", ("Melanesia",), 5),
        ("select * from country where subregion=?;", ("Micronesia",), 7),
        ("select * from country where subregion=?;", ("Middle Africa",), 9),
        ("select * from country where subregion=?;", ("Northern Africa",), 7),
        ("select * from country where subregion=?;", ("Northern America",), 7),
        ("select * from country where subregion=?;", ("Northern Europe",), 16),
        ("select * from country where subregion=?;", ("Polynesia",), 10),
        ("select * from country where subregion=?;", ("South America",), 14),
        ("select * from country where subregion=?;", ("South-eastern Asia",), 11),
        ("select * from country where subregion=?;", ("Southern Africa",), 5),
        ("select * from country where subregion=?;", ("Southern Asia",), 9),
        ("select * from country where subregion=?;", ("Southern Europe",), 18),
        ("select * from country where subregion=?;", ("Western Africa",), 17),
        ("select * from country where subregion=?;", ("Western Asia",), 17),
        ("select * from country where subregion=?;", ("Western Europe",), 9),
    ],
)
def test_db_subregion(query, args, results):
    """Querying the database"""
    assert len(read_db(query, args)) == results


@pytest.mark.parametrize(
    "query, args, results",
    [
        ("select distinct continental_region from country;", tuple(), 6),
        ("select * from country where continental_region=?;", ("Africa",), 59),
        ("select * from country where continental_region=?;", ("Americas",), 56),
        ("select * from country where continental_region=?;", ("Antarctica",), 5),
        ("select * from country where continental_region=?;", ("Asia",), 50),
        ("select * from country where continental_region=?;", ("Europe",), 53),
        ("select * from country where continental_region=?;", ("Oceania",), 27),
    ],
)
def test_db_continental_region(query, args, results):
    """Querying the database"""
    assert len(read_db(query, args)) == results


if __name__ == "__main__":
    pytest.main(["-v", __file__])

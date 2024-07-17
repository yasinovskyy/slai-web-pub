#!/usr/bin/env python3
"""
Using pytest-flask to test the back end

@authors: Roman Yasinovskyy
@version: 2024.7
"""

import pytest


def test_index_get(client):
    """GET should work"""
    assert client.get("/").status_code == 200


def test_index_post(client):
    """POST without any data should trigger query defaults"""
    assert client.post("/").status_code == 200


@pytest.mark.parametrize(
    "country",
    [
        ("Åland Islands"),
        ("Bahamas"),
        ("United States Virgin Islands"),
        ("United States"),
        ("Ukraine"),
    ],
)
def test_country_query(client, country):
    """Various countries should be handled"""
    assert (
        client.post("/", data=dict(country_query="on", country=country)).status_code
        == 200
    )


@pytest.mark.parametrize(
    "country",
    [
        ("Genovia"),
        ("Hobbiton"),
        ("Narnia"),
        ("Neverland"),
        ("Wakanda"),
    ],
)
def test_country_query_error(client, country):
    """Various fictional countries should be handled"""
    assert (
        client.post("/", data=dict(country_query="on", country=country)).status_code
        == 404
    )


@pytest.mark.parametrize(
    "region",
    [
        ("Australia and New Zealand"),
        ("Caribbean"),
        ("Central America"),
        ("Central Asia"),
        ("Eastern Africa"),
        ("Eastern Asia"),
        ("Eastern Europe"),
        ("Melanesia"),
        ("Micronesia"),
        ("Middle Africa"),
        ("Northern Africa"),
        ("Northern America"),
        ("Northern Europe"),
        ("Polynesia"),
        ("South America"),
        ("South-eastern Asia"),
        ("Southern Africa"),
        ("Southern Asia"),
        ("Southern Europe"),
        ("Western Africa"),
        ("Western Asia"),
        ("Western Europe"),
    ],
)
def test_region_query(client, region):
    """Various regions should be handled"""
    assert (
        client.post("/", data=dict(region_query="on", region=region)).status_code == 200
    )


@pytest.mark.parametrize(
    "region",
    [
        ("Central Africa"),
        ("Middle East"),
        ("Northern Asia"),
        ("Southeast Asia"),
        ("Western America"),
    ],
)
def test_region_query_error(client, region):
    """Various fictional regions should be handled"""
    assert (
        client.post("/", data=dict(region_query="on", region=region)).status_code == 404
    )


@pytest.mark.parametrize(
    "continent",
    [
        ("Africa"),
        ("Americas"),
        ("Antarctica"),
        ("Asia"),
        ("Europe"),
        ("Oceania"),
    ],
)
def test_continent_query(client, continent):
    """Various continents should be handled"""
    assert (
        client.post(
            "/", data=dict(continent_query="on", continent=continent)
        ).status_code
        == 200
    )


@pytest.mark.parametrize(
    "continent",
    [
        ("Alagaësia"),
        ("Atlantis"),
        ("Gondwana"),
        ("Pangea"),
        ("Vaalbara"),
    ],
)
def test_continent_query_error(client, continent):
    """Various fictional continents should be handled"""
    assert (
        client.post(
            "/", data=dict(continent_query="on", continent=continent)
        ).status_code
        == 404
    )


if __name__ == "__main__":
    pytest.main(["-v", __file__])

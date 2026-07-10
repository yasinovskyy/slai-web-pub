#!/usr/bin/env python3
"""
Using pytest-flask to test the back end

@authors: Roman Yasinovskyy
@version: 2026.7
"""

from itertools import product
import pytest


@pytest.mark.easy
def test_status_get(client) -> None:
    """GET should work"""
    assert client.get("/").status_code == 200


@pytest.mark.parametrize(
    "language, category",
    list(
        product(
            ["cs", "de", "en", "es", "eu", "fr", "gl", "hu", "it", "lt", "pl", "sv"],
            ["all", "chuck", "neutral"],
        )
    ),
)
@pytest.mark.medium
def test_status_post(client, language: str, category: str) -> None:
    """POST with various combinations of language/category should work"""
    assert client.post("/", data=dict(language=language, category=category)).status_code == 200


@pytest.mark.medium
def test_status_post_default(client) -> None:
    """POST without any data should trigger defaults"""
    assert client.post("/").status_code == 200


if __name__ == "__main__":
    pytest.main(["-v", __file__])

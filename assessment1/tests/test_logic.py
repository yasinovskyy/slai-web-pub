#!/usr/bin/env python3
"""
Using pytest-flask to test the application logic

@authors: Roman Yasinovskyy
@version: 2026.7
"""

from itertools import product, permutations

import pytest
from joker.logic import query


@pytest.mark.easy
def test_get_default_joke() -> None:
    """Query called without any parameters should return a single joke"""
    assert len(query()) == 1


@pytest.mark.parametrize(
    "language, category",
    list(
        product(
            ["cs", "de", "en", "es", "hu", "it", "pl"],
            ["all", "chuck", "neutral"],
        )
    ),
)
@pytest.mark.easy
def test_get_a_joke(language: str, category: str) -> None:
    """Various combinations of language/category should be handled and return a single joke"""
    assert len(query(language, category)) == 1


@pytest.mark.parametrize(
    "language, category",
    list(
        product(
            ["eu", "fr", "gl", "lt", "sv"],
            ["all", "neutral"],
        )
    ),
)
@pytest.mark.easy
def test_get_a_neutral_joke(language: str, category: str) -> None:
    """Various combinations of language/category should be handled and return a single joke"""
    assert len(query(language, category)) == 1


@pytest.mark.parametrize(
    "language, category, number",
    list(
        product(
            ["cs", "de", "en", "es", "it", "pl"],
            ["all", "chuck", "neutral"],
            range(1, 10),
        )
    ),
)
@pytest.mark.medium
def test_get_n_jokes(language: str, category: str, number: int) -> None:
    """Some combinations of language/category should return multiple jokes"""
    assert len(query(language, category, str(number))) == number


@pytest.mark.parametrize(
    "language, category, number",
    [
        ("cs", "all", 41),
        ("de", "all", 127),
        ("en", "all", 283),
        ("es", "all", 44),
        ("eu", "all", 5),
        ("fr", "all", 26),
        ("gl", "all", 14),
        ("hu", "all", 9),
        ("it", "all", 159),
        ("lt", "all", 30),
        ("pl", "all", 174),
        ("sv", "all", 41),
        ("cs", "chuck", 12),
        ("de", "chuck", 68),
        ("en", "chuck", 103),
        ("es", "chuck", 16),
        ("hu", "chuck", 1),
        ("it", "chuck", 87),
        ("pl", "chuck", 99),
        ("cs", "neutral", 29),
        ("de", "neutral", 59),
        ("en", "neutral", 180),
        ("es", "neutral", 28),
        ("eu", "neutral", 5),
        ("fr", "neutral", 26),
        ("gl", "neutral", 14),
        ("hu", "neutral", 8),
        ("it", "neutral", 72),
        ("lt", "neutral", 30),
        ("pl", "neutral", 75),
        ("sv", "neutral", 41),
    ],
)
@pytest.mark.medium
def test_get_all_jokes(language: str, category: str, number: int) -> None:
    """There is a limited number of jokes in each category/language"""
    assert len(query(language, category, "2026")) == number


@pytest.mark.parametrize(
    "language",
    ["".join(code) for code in permutations("abjkmoqwxyz", 2)],
)
@pytest.mark.hard
def test_language_error(language: str) -> None:
    """There are no only jokes in some languages"""
    with pytest.raises(ValueError) as excinfo:
        assert query(language, "neutral")
    assert str(excinfo.value) == "There are no jokes in the chosen language: " + language + "."


@pytest.mark.parametrize(
    "language",
    ["eu", "fr", "gl", "lt", "sv"],
)
@pytest.mark.hard
def test_category_error(language: str) -> None:
    """There are no Chuck Norris jokes in some languages"""
    with pytest.raises(ValueError) as excinfo:
        assert query(language, "chuck")
        assert excinfo.value == "There are no jokes in the chosen category: chuck."


if __name__ == "__main__":
    pytest.main(["-v", __file__])

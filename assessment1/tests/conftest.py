#!/usr/bin/env python3
"""
Backend test configuration

@authors: Roman Yasinovskyy
@version: 2026.7
"""

import pytest
from joker import create_app

TIMEOUT = 1000


@pytest.fixture()
def app():
    app = create_app()
    app.config.update(
        {"TESTING": True},
    )
    yield app


@pytest.fixture()
def client(app):
    return app.test_client()


@pytest.fixture()
def runner(app):
    return app.test_cli_runner()


def pytest_configure(config):
    config.addinivalue_line("markers", "easy: easy cases")
    config.addinivalue_line("markers", "medium: medium-complexity cases")
    config.addinivalue_line("markers", "hard: tests that verify error handling")

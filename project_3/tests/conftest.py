#!/usr/bin/env python3
"""
Backend test configuration

@authors: Roman Yasinovskyy
@version: 2024.7
"""

import pytest
from geography import create_app


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

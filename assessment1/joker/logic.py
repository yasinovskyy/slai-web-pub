#!/usr/bin/env python3
"""
Serving `pyjokes` via templates
Application logic

@author:
@version: 2026.7
"""

import random

import pyjokes
from pyjokes.exc import CategoryNotFoundError, LanguageNotFoundError


def query(
    language: str = "en",
    category: str = "neutral",
    number: str = "1",
) -> list[str]:
    """Return a list of jokes"""
    # TODO: Implement this function
    ...

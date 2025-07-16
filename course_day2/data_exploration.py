#!/usr/bin/env python3

from typing import Any
import csv


def read_csv(filename: str) -> list[dict[str, Any]]:
    with open(filename, "r", encoding="utf-8") as csv_file:
        return [record for record in csv.DictReader(csv_file)]

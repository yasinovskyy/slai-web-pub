#!/usr/bin/env python3
"""
Data handling demo

@author: Roman Yasinovskyy
@version: 2025.7
"""


def read_txt(filename: str, state: str) -> None:
    """Read data from a text file

    :param filename: name of a file to open
    :param state: state to filter by
    """
    with open(filename, "r", encoding="utf-8") as input_file:
        data = input_file.readlines()
        for college in data:
            college_name = college.split("(")[0].strip()
            college_state = college.split(",")[1].strip()[:-1]
            if college_state == state:
                print(college_name)


read_txt("acm.txt", "Iowa")

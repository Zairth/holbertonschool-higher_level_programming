#!/usr/bin/python3
"""Defines a function that append a text in a file"""


def append_write(filename="", text=""):
    """
    Append a string in a file,
    If it doesnt exist, create it and write in it
    If it exist, append in it
    """

    char_written = 0

    with open(filename, "a", encoding="utf-8") as file:
        char_written = file.write(text)

    return char_written

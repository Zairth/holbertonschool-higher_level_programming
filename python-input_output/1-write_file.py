#!/usr/bin/python3
"""Defines a function that write or overwrite a string in a file"""


def write_file(filename="", text=""):
    """
    Write a string in a file,
    If it doesnt exist, create it and write in it
    If it exist, overwrit it
    """

    char_written = 0

    with open(filename, "w", encoding="utf-8") as file:
        char_written += file.write(text)

    return char_written

#!/usr/bin/python3
"""Defines a function that reads text file"""


def read_file(filename=""):
    """Open, read and print the contents of a file to stdout"""

    with open(filename, "r", encoding="utf-8") as file:
        text_file = file.read()
        print("{}".format(text_file), end="")

    return text_file

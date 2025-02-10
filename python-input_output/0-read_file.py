#!/usr/bin/python3


def read_file(filename=""):
    """Open, Read, And write a file in the stdout"""

    with open(filename, "r") as file:
        print("{}".format(file.read()), end="")

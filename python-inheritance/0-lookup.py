#!/usr/bin/python3


"""
Function that return a list of available attribute and method of an object

Args:
    obj: The object to return the list

Returns:
    a dir of available attributes and methods of the args
"""


def lookup(obj):
    return list(dir(obj))

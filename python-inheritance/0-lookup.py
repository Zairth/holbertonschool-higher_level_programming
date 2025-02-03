#!/usr/bin/python3


"""
Function that return a list of available attribute and method of an object
"""


def lookup(obj):
    return list(dir(obj))

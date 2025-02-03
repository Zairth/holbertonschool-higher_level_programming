#!/usr/bin/python3
def lookup(obj):
    """
    Function that return a list of available attribute and method of an object

    Args:
        obj: The object to return the list

    Returns:
        a dir of available attributes and methods of the args
    """

    return list(dir(obj))

#!/usr/bin/python3


def lookup(obj):
    """Returns the list of available attributes and methods of an object.

    Args:
        obj: The object whose attributes and methods are to be returned.

    Returns:
        A list of string representing the attributes and methods of the object.
    """

    return list(dir(obj))

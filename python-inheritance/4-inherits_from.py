#!/usr/bin/python3
"""4-inherits_from.py
"""


def inherits_from(obj, a_class):
    """Verify if the object is an instance of a class that inherited"""

    if isinstance(obj, a_class):
        if type(obj) is not a_class:
            return True

    return False

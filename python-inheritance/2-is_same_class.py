#!/usr/bin/python3
"""2-is_same_class.py
"""


def is_same_class(obj, a_class):
    """Verify if it is exactly the same type as specified"""

    if type(obj) is a_class:
        return True

    return False

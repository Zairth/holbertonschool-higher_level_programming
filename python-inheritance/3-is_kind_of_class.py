#!/usr/bin/python3
"""3-is_kind_of_class.py
"""


def is_kind_of_class(obj, a_class):
    """Verify if obj have the class or subclass as a_class"""

    if isinstance(obj, a_class):
        return True

    return False

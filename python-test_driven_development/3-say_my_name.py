#!/usr/bin/python3
"""
Print le nom prénom
"""


def say_my_name(first_name, last_name=""):
    """
    Print le nom/prénom
    Args:
        first_name (str): Le prénom
        last_name (str): Le nom de famille
    Returns:
        None
    Exemple:
        >>> say_my_name("John", "Smith")
        My name is John Smith
    """

    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")
    print("My name is {} {}".format(first_name, last_name))

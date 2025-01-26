#!/usr/bin/python3
"""
Print un carré de la taille de size
"""


def print_square(size):
    """
    Print un carré de la taille de size
    Args:
        size (int/float): la taille du carré
    Returns:
        None
    Exemple:
        >>> print_square(2)
        ##
        ##
    """

    if not isinstance(size, (int, float)):
        raise TypeError("size must be an integer")
    if size < 0:
        if isinstance(size, float):
            raise TypeError("size must be an integer")
        raise ValueError("size must be >= 0")

    for i in range(size):
        for j in range(size):
            print("#", end="")
        print("")

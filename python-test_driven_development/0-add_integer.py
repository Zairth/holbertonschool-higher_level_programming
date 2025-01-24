#!/usr/bin/python3
"""
Adding two integers
"""
def add_integer(a, b=98):
    """
    Additionne deux nombres.
    Args:
        a (int): Premier nombre
        b (int): Deuxième nombre
    Returns:
        int: La somme de a et b
    Exemple:
        >>> add_integer(2, 3)
        5
        >>> add_integer(4, 3)
        7
    """

    result = 0

    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")

    a = int(a)
    b = int(b)
    result = a + b

    return result

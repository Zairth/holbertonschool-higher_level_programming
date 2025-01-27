#!/usr/bin/python3
"""
Create a square
"""


class Square:
    """
    Create a new square

    Attributes:
        __size (int): Private instance attribute size of the square
    """

    def __init__(self, __size=0):
        """
        Init the square with a size

        Args:
            __size: The size of the square

        Returns:
            The size, or raise an error
        """

        if not isinstance(__size, int):
            raise TypeError("size must be an integer")
        if __size < 0:
            raise ValueError("size must be >= 0")
        self.__size = __size

    def area(self):
        """
        Returning the area of the square

        Returns:
            The area of the square
        """

        return self.__size * self.__size

#!/usr/bin/python3
"""
Create a square
"""


class Square:
    """
    Create a new square

    Attributes:
        size (int): instance attribute size of the square
    """

    def __init__(self, size=0):
        """
        Init the square with a size

        Args:
            size: The size of the square
        """

        self.size = size

    @property
    def size(self):
        """
        Getter to gain acces of __size

        Returns:
            The size of the square
        """

        return self.__size

    @size.setter
    def size(self, __size):
        """Setter to modificate __size with verification"""

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

    def my_print(self):
        """
        Print a square
        """

        if self.size == 0:
            print("")
        else:
            for i in range(self.size):
                for j in range(self.size):
                    print("#", end="")
                print("")

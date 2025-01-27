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

    def __init__(self, size=0, position=(0, 0)):
        """
        Init the square with a size

        Args:
            size: The size of the square
        """

        self.size = size
        self.position = position

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

    @property
    def position(self):
        """
        Getter to gain acces of __size

        Returns:
            The size of the square
        """

        return self.__position

    @position.setter
    def position(self, __position):
        """Setter to modificate __size with verification"""

        for tuple in __position:
            if not isinstance(tuple, int):
                raise TypeError("position must be a tuple of \
2 positive integers")
            if tuple < 0:
                raise TypeError("position must be a tuple of \
2 positive integers")

        self.__position = __position

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

        for i in range(self.position[1]):
            print("")

        if self.size == 0:
            print("")
        else:
            for i in range(self.size):
                for i in range(self.position[0]):
                    print(" ", end="")
                for j in range(self.size):
                    print("#", end="")
                print("")

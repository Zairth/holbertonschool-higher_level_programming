#!/usr/bin/python3
"""10-square.py
"""


Rectangle = __import__("9-rectangle").Rectangle


class Square(Rectangle):
    """
    Create a new instance inherited from Rectangle
    """

    def __init__(self, size):
        """Init the Square"""

        self.integer_validator("size", size)
        super().__init__(size, size)

        self.__size = size

    def area(self):
        """Return the area of the square"""

        return self.__size * self.__size

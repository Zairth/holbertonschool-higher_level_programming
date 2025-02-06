#!/usr/bin/python3
"""8-rectangle.py
"""


class BaseGeometry():
    """
    Create a new instance
    """

    def area(self):
        """Raise an exception"""

        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validates that value is a positive integer."""

        if not isinstance(value, int):
            raise TypeError("{} must be an integer".format(name))

        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))


class Rectangle(BaseGeometry):
    """
    Create a new instance inherited from BaseGeometry

    Attributes:
        width (int): width of the rectangle
        height (int): the height of the rectangle
    """

    def __init__(self, width, height):
        """Init the Rectangle"""

        super().integer_validator("height", height)
        super().integer_validator("width", width)
        self.__height = height
        self.__width = width

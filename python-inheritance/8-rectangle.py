#!/usr/bin/python3
"""8-rectangle.py
"""


BaseGeometry = __import__("7-base_geometry").BaseGeometry


class Rectangle(BaseGeometry):
    """
    Create a new instance inherited from BaseGeometry

    Attributes:
        width (int): width of the rectangle
        height (int): the height of the rectangle
    """

    def __init__(self, width, height):
        """Init the Rectangle"""

        self.integer_validator("height", height)
        self.integer_validator("width", width)

        self.__height = height
        self.__width = width

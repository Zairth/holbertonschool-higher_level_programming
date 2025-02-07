#!/usr/bin/python3
"""9-rectangle.py
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

    def area(self):
        """Return the area of the rectangle"""

        return self.__height * self.__width

    def __print__(self):
        """Print a personnalized message"""

        print("[Rectangle] {}/{}".format(self.__width, self.__height))

    def __str__(self):
        """Return a personnalized message"""
        return f"[Rectangle] {self.__width}/{self.__height}"

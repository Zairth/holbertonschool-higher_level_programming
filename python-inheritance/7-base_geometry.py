#!/usr/bin/python3
"""7-base_geometry.py
"""


class BaseGeometry():
    """
    Create a new instance
    """

    def area(self):
        """Raise an exception"""

        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Raise an exception"""

        if not isinstance(value, int):
            raise TypeError("<name> must be an integer")

        if value <= 0:
            raise ValueError("<name> must be greater than 0")

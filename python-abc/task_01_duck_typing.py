#!/usr/bin/python3
from abc import ABC, abstractmethod
import math


class Shape(ABC):
    """Abstract class inherited from ABC"""

    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass


class Circle(Shape):
    """Class inherited from Animal"""

    def __init__(self, radius):
        """Init the instance with Radius"""

        radius = abs(radius)
        self.radius = radius

    def area(self):
        """Abstract method that implemente the parent method"""

        return math.pi * self.radius ** 2

    def perimeter(self):
        """Abstract method that implemente the parent method"""

        return 2 * math.pi * self.radius


class Rectangle(Shape):
    """Class inherited from Animal"""

    def __init__(self, height, width):
        """Init the instance with Height, and width"""

        self.height = height
        self.width = width

    def area(self):
        """Abstract method that implemente the parent method"""

        return self.height * self.width

    def perimeter(self):
        """Abstract method that implemente the parent method"""

        return 2 * (self.height + self.width)


def shape_info(instance):
    """Function that print area and perimeter of instance class"""

    print("Area: {}".format(instance.area()))
    print("Perimeter: {}".format(instance.perimeter()))

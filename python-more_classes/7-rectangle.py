#!/usr/bin/python3
"""
Create a rectangle
"""


class Rectangle:
    """
    Create a new Rectangle

    Attributes:
        width (int): The Width of the rectangle
        height (int): The Height of the rectangle
        number_of_instances (int): The number of the current living instance
        print_symbol (str): The symbole to use for printing the Rectangle
    """

    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """
        Init the Rectangle with a size

        Args:
            width: The width of the rectangle
            height: The height of the rectangle
        """

        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        """
        Getter to gain acces of __width

        Returns:
            The width of the Rectangle
        """

        return self.__width

    @width.setter
    def width(self, __width):
        """Setter to modificate __width with verification"""

        if not isinstance(__width, int):
            raise TypeError("width must be an integer")
        if __width < 0:
            raise ValueError("width must be >= 0")

        self.__width = __width

    @property
    def height(self):
        """
        Getter to gain acces of __height

        Returns:
            The height of the Rectangle
        """

        return self.__height

    @height.setter
    def height(self, __height):
        """Setter to modificate __height with verification"""

        if not isinstance(__height, int):
            raise TypeError("height must be an integer")
        if __height < 0:
            raise ValueError("height must be >= 0")

        self.__height = __height

    def area(self):
        """
        Returning the area of the Rectangle

        Returns:
            The area of the rectangle
        """

        return self.height * self.width

    def perimeter(self):
        """
        Returning the perimeter of the Rectangle

        Returns:
            The perimeter of the rectangle
        """

        if self.height == 0 or self.width == 0:
            return 0

        return 2 * (self.height + self.width)

    def __str__(self):
        """
        Return a string representation of the Rectangle

        Returns:
            The string representation of the Rectangle
        """

        rect_print = ""
        if self.height == 0 or self.width == 0:
            return rect_print
        for i in range(self.height):
            for j in range(self.width):
                if isinstance(self.print_symbol, list):
                    rect_print += repr(self.print_symbol)
                else:
                    rect_print += self.print_symbol
            if i < self.height - 1:
                rect_print += "\n"
        return rect_print

    def __repr__(self):
        """
        Return a string representation for recreation via eval()

        Returns:
            The string representation for the new instance
        """

        return f"Rectangle({self.width}, {self.height})"

    def __del__(self):
        """
        Print a message when the function del is used
        """

        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")

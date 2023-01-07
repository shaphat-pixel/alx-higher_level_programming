#!/usr/bin/python3

"""A rectangle class"""


class Rectangle:
    """ Rectangle class"""

    def __init__(self, width=0, height=0):
        """Instantiation"""
        self.width = width
        self.height = height

    @property
    def width(self):
        """retrieve width"""
        return self.__width

    @width.setter
    def width(self, value):
        """set width"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")

        self.__width = value

    @property
    def height(self):
        """retrieve height """
        return self.__height

    @height.setter
    def height(self, value):
        """set height"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        return self.width * self.height

    def perimeter(self):
        if self.width == 0 or self.height == 0:
            return 0
        return (2*self.width) + (2*self.height)

    def __str__(self):
        if self.width == 0 or self.height == 0:
            return ("")
        rect = []

        for i in range(self.height):
            [rect.append('#') for j in range(self.width)]
            if i != self.height - 1:
                rect.append("\n")
        return ("".join(rect))

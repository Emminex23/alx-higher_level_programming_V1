#!/usr/bin/python3
"""Defines a rectangle class"""


class Rectangle:
    """Represents a rectangle"""
    def __init__(self, width=0, height=0):
        """
            Initializes a new rectangle

            args:
             height (int): The height of the new rectangle
             width (int): The width of the new rectangle
        """
        self.height = height
        self.width = width

    @property
    def width(self):
        """Get/set the width of the rectangle"""
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Get/set the height of the rectangle"""
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Returns the value of the area of the rectangle"""
        return (self.height * self.width)

    def perimeter(self):
        """Returns the value of the perimeter of the rectangle"""
        if self.width == 0 or self.height == 0:
            return 0
        return ((self.height * 2) + (self.width * 2))

    def __str__(self):
        """Return the printable representation of the Rectangle.
        Represents the rectangle with the # character.
        """
        if self.width == 0 or self.height == 0:
            return ("")

        rectangle = ""
        for i in range(self.height):
            for j in range(self.width):
                rectangle += "#"
            rectangle += "\n"
        rectangle = rectangle[:-1]
        return rectangle

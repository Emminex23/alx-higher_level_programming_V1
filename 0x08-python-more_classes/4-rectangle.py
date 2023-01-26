#!/usr/bin/python3
"""This defines a rectangle class"""


class Rectangle:
    """This represents a rectangle"""
    def __init__(self, width=0, height=0):
        """This initializes a new rectangle.
            Args:
                width (int): This is the width of the new rectangle
                height (int): This is the height of the new rectangle
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """This gets/sets the width of the rectangle"""
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
        """This sets or gets the height of the rectangle"""
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """This returns the area of the rectangle"""
        return (self.width * self.height)

    def perimeter(self):
        """This returns the perimeter of the rectangle"""
        if self.width == 0 or self.height == 0:
            return 0
        return 2 * (self.width + self.height)

    def __str__(self):
        """This prints the rectangle with the character #"""
        if self.width == 0 or self.height == 0:
            return ""
        rectangle = ""
        for i in range(self.height):
            for j in range(self.width):
                rectangle += "#"
            rectangle += "\n"
        rectangle = rectangle[:-1]
        return rectangle

    def __repr__(self):
        return "Rectangle({}, {})".format(self.width, self.height)

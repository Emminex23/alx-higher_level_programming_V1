#!/usr/bin/python3
"""This module defines a Rectangle"""


class Rectangle:
    """This class represents a rectangle"""
    def __init__(self, width=0, height=0):
        """
            This initializes a new rectangle.
            Args:
                width (int): This is the width of the new rectangle
                height (int): This is the height of the new rectangle
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """This get/sets the width of the rectangle"""
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
        """Gets/sets the height of rectangle"""
        return self.__height

    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """returns the area of the rectangle"""
        return (self.width * self.height)

    def perimeter(self):
        """This method returns the perimeter of the rectangle"""
        if self.width == 0 or self.height == 0:
            return 0
        return 2 * (self.width + self.height)

    def __str__(self):
        """
            This method prints the string format of the rectangle
            using the character #
        """
        if self.width == 0 or self.height == 0:
            return ""
        rectangle = ""
        for i in range(self.height):
            for j in range(self.width):
                rectangle += '#'
            rectangle += "\n"
        rectangle = rectangle[:-1]
        return rectangle

    def __repr__(self):
        """
            This method return a string representation of the rectangle
            to be able to recreate a new instance by using eval()
        """
        return f"Rectangle({self.width}, {self.height})"

    def __del__(self):
        print("Bye rectangle...")

#!/usr/bin/python3
"""Defines a rectangle class"""

class Rectangle:
    """Represents a rectangle"""
    def __init__(self, height=0, width=0):
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
        self.__height =  value

    def area(self):
        """Returns the value of the area of the rectangle"""
        return (self.__height * self.__width)

    def perimeter(self):
        """Returns the value of the perimeter of the rectangle"""
        if self.__width == 0 or self.__height == 0:
            return 0
        return ((self.__height * 2) + (self.__width * 2))

    def __str__(self):
        """
            This prints a rectangle using
            the # character
        """
        if self.__width == 0 or self.__height == 0:
            return ("")
        rectangle = ""
        for i in range(self.__height):
            for j in range(self.__width):
                rectangle += "#"
            rectangle += "\n"
        rectangle = rectangle[:-1]
        return rectangle

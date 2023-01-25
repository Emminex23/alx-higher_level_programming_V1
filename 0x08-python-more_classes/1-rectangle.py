#!/usr/bin/python3
class Rectangle:
    def __init__(self, width=0):
        self.width = width

    def width(self):
        return self.__width

    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    def __init__(self, height=0):
        self.height = height

    def height(self):
        return self.__height

    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self._height = value

    def __init__(self, width=0, height=0):
        self.__height = height
        self.__width = width

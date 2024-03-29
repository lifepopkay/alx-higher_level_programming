#!/usr/bin/python3

"""
This module is composed by a class that defines a Rectangle

"""


class Rectangle():
    """
        Additional argument to first class created

    """
    def __init__(self, width=0, height=0):
        self.height = height
        self.width = width
        

    @property
    def width(self):
        """
            This returns width

        """
        return self.__width

    @width.setter
    def width(self, value):
        """
            this define width

            Raise:
                TypeError if not integer
                ValueError if less than 0

        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >=0")
        self.__width = value

    @property
    def height(self):
        """
            This returns height

        """
        return self.__height

    @height.setter
    def height(self, value):

        """
            This defines height

         Raise:
                TypeError if height is not an integer
                ValueError if height is less than 0
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")

        self.__height = value

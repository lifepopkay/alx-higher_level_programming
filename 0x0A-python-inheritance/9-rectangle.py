#!/usr/bin/python3
"""
    8-rectangle: class Rectangle from BaseGeomerty
"""


BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """
        Class inherit from Geometry
        Args:
            width (int): width of rectangle
            height (int): height of rectangle
        Methods:
            __init__ - initialises the Rectangle.
    """

    def __init__(self, width, height):
        super().integer_validator("width", width)
        super().integer_validator("height", height)

        self.__width = width
        self.__height = height

    def area(self):
        """ Method that returns the area of the instance"""

        return self.__width * self.__height

    def __str__(self):
        """ Special method that returns the printable string """

        return "[Rectangle] {:d}/{:d}".format(self.__width, self.__height)

#!/usr/bin/python3
"""
   11-square: inherits from Rectangle
"""

Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """
        initialises the size

        Method:
                __init__ : this receives the intances
        Agrs:
                size: the size of square
        Return:
                Area of the squar`e
    """
    def __init__(self, size):
        """ initialises the size """

        super().integer_validator("size", size)
        self.__size = size
        super().init(self.__size, self.__size)

    def area(self):
        """ Return the area of Square """

        return self.__size * self.__size

    def __str__(self):
        """ Special method that returns the printable string """

        return "[Square] {:d}/{:d}".format(self.__size, self.__size)

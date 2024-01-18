#!/usr/bin/python3
"""
   10-square: inherits from Rectangle
"""

Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """
        initiasiles the size

        Method:
                __init__ - initialise the square
        Args:
                size (int): the size of square
        Return:
                Area of the square
    """
    def __init__(self, size):
        """
            initialises square
        """

        super().integer_validator("size", size)
        self.__size = size
        super().init(self.__size, self.__size)

    def area(self):
        """
            Return the area of square
        """

        return super().area()

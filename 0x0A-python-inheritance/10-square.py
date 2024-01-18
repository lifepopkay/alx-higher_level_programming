#!/usr/bin/python3
"""
   10-square: inherits from Rectangle
"""



class Square(Rectangle):
    """
        initiasiles the size

        Method:
                __init__ : this receives the intances
        Agrs:
                size: the size of square
        Return:
                Area of the squar`e
    """
    def __init__(self, size):

        super().integer_validator("size", size)
        self.__size = size
        super().init(self.__size, self.__size)

    def area(self):
        return self.__size * self.__size

    def __str__(self):
        """ Special method that returns the printable string """

        rreturn "[Rectangle] {:d}/{:d}".format(self.__size, self.__size)

#!/usr/bin/python3
"""THis class gives the area of a square"""


class Square:
    """
        Square: defines a square.
        Attributes:
            size (no type or value identification): size of square.
        Method:
                __init__ : init of size attribute for each instance.
    """

    def __init__(self, size=0):

        """ Initialization of attributes for instances
            Args:
                size (int): size of the square.
        """

        if not isinstance(size, int):
            raise TypeError("size must be an interger")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

    def area(self):
        return self.__size ** 2

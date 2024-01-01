#!/usr/bin/python3
""" This class set and get """


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
        self.__size = size

    @property
    def size(self):

        """ This is getter gets size"""

        return self.__size

    @size.setter
    def size(self, value):

        """ This set the value"""

        if not isinstance(value, int):
            raise TypeError("size must be an interger")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):

        """This area of the value"""

        return self.__size * self.__size

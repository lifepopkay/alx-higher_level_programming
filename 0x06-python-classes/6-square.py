#!/usr/bin/python3


class Square:
    """
        Square: defines a square.
        Attributes:
            size (int): size of square.
        Method:
                __init__ : init of size attribute for each instance.
    """
    def __init__(self, size=0, position=(0, 0)):
        """ Initialization of attributes for instances
            Args:
                size (int): size of the square.
                position (int tuple): position of the square
        """
        self.size = size
        self.position = position

    @property
    def size(self):
        """ getter function for private attribute size.
            Returns:
                size.
        """
        return self.__size

    @size.setter
    def size(self, value):
        """ setter function for private attribute size.
            Args:
                value: size value to set to
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        return self.__position

    @position.setter
    def position(self, value):
        if (type(value) != tuple or
                len(value) != 2 or
                not all(isinstance(i, int) for i in value) or
                not all(i >= 0 for i in value)):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        return self.__size * self.__size

    def my_print(self):
        if self.__size == 0:
            print()
        else:
            for _ in range(self.__position[1]):
                print()
            for _ in range(self.__size):
                print(" " * self.__position[0] + "#" * self.__size)

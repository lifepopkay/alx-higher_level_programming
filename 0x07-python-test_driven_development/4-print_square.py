#!/usr/bin/python3
""" 4-print_square"""


def print_square(size):
    """
        function prints a square

        args size - length of the square
    """
    if type(size) != int:
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    if type(size) == float and size < 0:
        raise TypeError("size must be an integer")

    for i in range(size):
        print("#" * size)

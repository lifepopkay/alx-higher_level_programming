#!/usr/bin/python3

"""
    BaseGeometry: an empty class
"""


class BaseGeometry():
    """
        this is a empty class

    """
    def area(Self):
        """
            this raise an exception

        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
            this validates the value input

            Args:
                    name:a string
                    value:integer to validate
            Return:
                    TypeError: if not integer
                    ValueError: if less or equal to 0
        """

        if not isinstance(value, int):
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))

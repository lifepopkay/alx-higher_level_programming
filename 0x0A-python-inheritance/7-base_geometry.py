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

        if not isinstance(self.value, int):
            raise TypeError("{self.value} must be an integer")
        if self.value <= 0:
            raise ValueError("{self.value} must be greater than 0")

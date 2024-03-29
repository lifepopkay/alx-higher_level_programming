#!/usr/bin/python3
"""
    This test if a class is inherited
"""


def is_kind_of_class(obj, a_class):
    """
         is_kind_of_class returns true if the object is instance of class.
                 Args:
                    obj (object): object.
                    a_class (class): class.
                Return: True or false
    """

    if isinstance(obj, a_class):
        return True
    return False

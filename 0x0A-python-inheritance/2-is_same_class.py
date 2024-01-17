#!/usr/bin/python3
"""
    Check if equal to the definde class
"""


def is_same_class(obj, a_class):
    """
        is same class:
                        Check if the object same with class specfied
                Args:
                        obj: object to check
                        a_class: specfied class
                Return:
                        True if eqaul
                        flase if not equal
    """

    if type(obj) is not a_class:
        return False
    else:
        return True

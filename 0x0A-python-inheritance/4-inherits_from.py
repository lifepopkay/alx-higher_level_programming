#!/usr/bin/python3
"""
    inherits_from: check inheritance relationships
"""


def inherits_from(obj, a_class):
    """
        This function checks if an objects is an instance of a class inherited

        Args:
            obj: object/instance
            a_class: class specified

        Return: True if inherited, false if otherwise
    """
    ty_obj = type(obj)
    if ty_obj != a_class and isinstance(obj, a_class):
        return True
    return False

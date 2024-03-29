#!/usr/bin/python3
"""
This module adds number only

"""


def add_integer(a, b=98):
    """Function to add  two numbers
    Args:
        a: first number
        b:second number
    Returns:
        The addition of the two numbers
    Raises:
        TypeError: if not integer

    """
    if not isinstance(a, int) and not isinstance(a, float):
        raise TypeError("a must be an integer")
    if not isinstance(b, int) and not isinstance(b, float):
        raise TypeError("b must be an integer")
    return (int(a) + int(b))

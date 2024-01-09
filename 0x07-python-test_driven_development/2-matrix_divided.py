#!/usr/bin/python3
"""
This Module is composed by a function that divides the numbers of a matrix
"""


def matrix_divided(matrix, div):
    """ Function that divides the integer/float numbers of a matrix
    Args:
        matrix: list of a lists of integers/floats
        div: number which divides the matrix
    Returns:
        A new matrix with the result of the division
    Raises:
        TypeError:If the elements of the matrix aren't lists
                If the elemetns of the lists aren't integers/floats
                If div is not an integer/float number
                If the lists of the matrix don't have the same size

        ZeroDivisionError: If div is zero

    """
    if not type(div) in (int, float):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZerorDivivsioError("division by zero")

    error = "matrix must be a matrix (list of lists) of integers/floats"

    if not matrix or not isinstance(matrix, list):
        raise TypeError(error)
    len_e = 0
    error_2 = "Each row of the matix must have the same size"
    for elems in matrix:
        if not elems or not isinstance(elems, list):
            raise TypeError(error)
        if len_e != 0 and len(elems) != len_e:
            raise TypeError(error_2)
        for num in elems:
            if not type(num) in (int, float):
                raise TypeError(error)

        len_e = len(elems)

    m = list(map(lambda x: list(map(lambda y: round(y / div, 2), x), matrix))

    return m

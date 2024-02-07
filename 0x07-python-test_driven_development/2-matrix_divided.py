#!/usr/bin/python3
"""
    matrix_divided : this divides the matrix of same lenght
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
        raise ZeroDivivsioError("division by zero")

    error_1 = "matrix must be a matrix (list of lists) of integers/floats"

    if matrix == [] or type(matrix) != list:
        raise TypeError(error_1)
    error_2 = "Each row of the matix must have the same size"

    if not isinstance(matrix, list):
        raise TypeError(error_1)
    new_matrix = []
    mul = []
    m_len = len(matrix)
    if m_len == 0:
        raise TypeError(error_1)
    else:
        if m_len == 1:
            for i in matrix[0]:
                if type(i) not in (int, float):
                    raise TypeError(error_2)
                mul.append(float("{:.2f}".format(i / div)))
            new_matrix.append(mul)
            return new_matrix
        elif mat_len == 2:
            if len(matrix[0]) != len(matrix[1]):
                raise TypeError(error_2)
        else:
            if len(matrix) == 3:
                if len(matrix[0]) != len(matrix[2]):
                    raise TypeError(error_2)
        for col in matrix:
            for row in col:
                if type(row) not in (int, float):
                    raise TypeError(error_1)

        for i in range(len(matrix)):
            d_list = list(map(lambda x: round(x / div, 2), matrix[i]))
            new_l.append(d_list)
        return new_l

#!/usr/bin/python3
"""
    100-matrix_mul
"""


def matrix_mul(m_a, m_b):
    """
        This function perform dot product of matrix

        Args:
            m_a: the first matrix
            m_b: the second matrix
        Return: The dot product

        Raises:TypeError: m_a and m_b must be list and list of lists
        m_a and m_b should contain only integers or float
        each row of m_a and m_b must be of the same size

        ValueError: m_a and m_b can't be empty
                    m_a and m_b can't be multiplied
    """

    if not isinstance(m_a, list):
        raise TypeError("m_a must be a list")

    if not isinstance(m_b, list):
        raise TypeError("m_b must be a list")

    for row in m_a:
        if not isinstance(row, list):
            raise TypeError("m_a must be a list of lists")

    for row in m_b:
        if not isinstance(row, list):
            raise TypeError("m_b must be a list of lists")

    if m_a == [] or m_a == [[]]:
        raise ValueError("m_a can't be empty")
    if m_b == [] or m_b == [[]]:
        raise ValueError("m_b can't be empty")

    if not all((type(ele) in (int, float))
                for ele in [i for row in m_a for i in row]):
        raise TypeError("m_a should contain only integers or floats")
    if not all((type(ele) in (int, float))
                for ele in [i for row in m_b for i in row]):
        raise TypeError("m_b should contain only integers or floats")

    if not all(len(row) == len(m_a[0]) for row in m_a):
        raise TypeError("each row of m_a must be of the same size")
    if not all(len(row) == len(m_b[0]) for row in m_b):
        raise TypeError("each row of m_b must be of the same size")

    if len(m_a[0]) != len(m_b):
        raise ValueError("m_a and m_b can't be multiplied")

    result = [[0 for _ in range(len(m_b[0]))] for _ in range(len(m_a))]
    for row in range(len(m_a)):
        for col in range(len(m_b[0])):
            for ele in range(len(m_b)):
                result[row][col] += m_a[row][ele] * m_b[ele][col]
    return result

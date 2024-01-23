#!/usr/bin/python3
"""
    12-pascal_triangle: defines a pascal's triangle functions
"""


def pascal_triangle(n):
    """
        Represent Pascal's Triangle of size n.

        Return:
                list of lists of integers representing the triangle.
    """
    if n <= 0:
        return []

    res = [[1]]  # first row which is always one
    for i in range(n - 1):  # the depth of our triangle
        # Temporary list for computation
        temp = [0] + res[-1] + [0]
        row = []
        for j in range(len(res[-1]) + 1):
            # length of each rows
            row.append(temp[j] + temp[j + 1])
        res.append(row)
    return res

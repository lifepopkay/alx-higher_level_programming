#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    new_mat = []
    for i in range(len(matrix)):
        result = list(map(lambda x: pow(x, 2), matrix[i]))
        new_mat.append(result)
    return new_mat

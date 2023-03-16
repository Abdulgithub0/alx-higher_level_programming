#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    length = len(matrix)
    inner_list = []
    outer_list = []
    for i in range(length):
        inner_list = list(map(lambda x: x * x, matrix[i]))
        outer_list.append(inner_list)
    return outer_list

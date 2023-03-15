#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    outer = len(matrix)
    new = [[]]
    for element in matrix:
        #inner = len(matrix[element])
        for i in matrix[element]:
            new.append(i * i)
    return new

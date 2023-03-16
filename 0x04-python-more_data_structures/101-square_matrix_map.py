#!/usr/bin/python3
def square_matrix_map(matrix=[]):
        return list(map(lambda y: list(map(lambda x: x*x, matrix[len(matrix) - 1])), matrix))

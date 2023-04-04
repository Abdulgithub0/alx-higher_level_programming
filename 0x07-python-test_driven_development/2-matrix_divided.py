#!/usr/bin/python3
""" function that divides all elements of a matrix"""


def matrix_divided(matrix, div):
    """defining the computation

        Args:
            matrix: parameter to hold nested list args
            div: integer value that will div each element of the matrix
        Return: a new nested list divided element of matrix
    """
    error = "matrix must be a matrix (list of lists) of integers/floats"
    if (type(matrix) == list):
        for row in matrix:
            if (row) and (type(row) == list):
                for d in row:
                    if not (isinstance(d, int) or isinstance(d, float)):
                        raise TypeError(error)
            else:
                raise TypeError(error)
    else:
        raise TypeError(error)
    if not (isinstance(div, int) or isinstance(div, float)):
        raise TypeError('div must be a number')
    if div == 0:
        raise ZeroDivisionError('division by zero')
    length = len(matrix[0])
    outer_l = []
    for row in matrix:
        if (len(row) == length):
            m = [div] * len(row)
            inner_l = list(map(lambda x, y: round(x / y, 2), row, m))
            outer_l.append(inner_l)
        else:
            raise TypeError("Each row of the matrix must have the same size")
    return outer_l

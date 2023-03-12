#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    length = len(matrix)
    for i in range(length):
        for j in range(len(matrix[i])):
            print('{:d}'.format(matrix[i][j]), end='')
            if (j + 1 == len(matrix[i])):
                    print('{}'.format(''))
            else:
                print(' ', end='')

#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    if not (matrix[0]):
        print('')
        return
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            print('{:d}'.format(matrix[i][j]), end='')
            if (j + 1 == len(matrix[i])):
                print('{}'.format(''))
            else:
                print(' ', end='')

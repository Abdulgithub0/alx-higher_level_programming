#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    lenght = len(my_list)
    if (type(my_list) is list):
        i = -1
        while (lenght != 0):
            print('{:d}'.format(my_list[i]))
            i -= 1
            lenght -= 1

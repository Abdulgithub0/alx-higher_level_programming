#!/usr/bin/python3
def replace_in_list(my_list, idx, element):
    lenght = len(my_list)
    if (idx > lenght - 1) or (idx < 0):
        return (my_list)
    for i in range(lenght):
        if (i == idx):
            my_list[i] = element
            return (my_list)

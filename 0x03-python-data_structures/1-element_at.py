#!/usr/bin/python3
def element_at(my_list, idx):
    lenght = len(my_list)
    if (idx > lenght or idx < 0):
        return (0)
    for i in range(lenght):
        if i == idx:
            return my_list[i]

#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    if not (my_list):
        return (None)
    else:
        new_list = []
        for num in my_list:
            if (num % 2 == 0):
                new_list += [1]
            else:
                new_list += [0]
        return (new_list)

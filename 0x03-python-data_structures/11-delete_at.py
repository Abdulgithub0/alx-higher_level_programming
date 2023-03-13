#!/usr/bin/python3
def delete_at(my_list=[], idx=0):
    length = len(my_list)
    if (length == 0):
        return (None)
    elif ((idx > length - 1) or (idx < 0)):
        return (my_list)
    else:
        for i in range(length):
            if (i == idx):
                del my_list[i]
        return (my_list)

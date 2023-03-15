#!/usr/bin/python3
def uniq_add(my_list=[]):
    no_dup = []
    for i in my_list:
        if i not in no_dup:
            no_dup.append(i)
    return sum(no_dup)

#!/usr/bin/python3
def only_diff_elements(set_1, set_2):
    new_set = set()
    for data in set_1:
        if data not in set_2:
            new_set.add(data)
    for data2 in set_2:
        if data2 not in set_1:
            new_set.add(data2)
    return new_set

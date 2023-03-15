#!/usr/bin/python3
def only_diff_elements(set_1, set_2):
    result = []
    for i in range(len(set_1)):
        if set_1[i] not in set_2:
            result.append(set_1[i])
    return result

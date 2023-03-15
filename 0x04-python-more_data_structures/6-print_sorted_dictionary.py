#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    sort_dict = []
    new_dict = dict()
    for key in a_dictionary.keys():
        sort_dict.append(key)
    sort_dict.sort()
    for key in sort_dict:
        if key in a_dictionary:
            print('{}: {}'.format(key, a_dictionary[key]))

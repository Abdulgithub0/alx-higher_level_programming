#!/usr/bin/python3
"""a function that finds a peak in a list of unsorted integers."""


def find_peak(list_of_integers):
    """find peak function definition"""
    lst = list_of_integers[:]
    len_l = len(lst)
    if (len_l == 0):
        return (None)
    if (len_l == 1):
        return (lst[0])
    list_of_integers.reverse()
    if (lst == list_of_integers):
        return lst[0]
    if (lst[0] > lst[1]):
        return lst[0]
    if (lst[-1] > lst[-2]):
        return lst[-1]
    for i in range(1, (len_l - 1)):
        if (lst[i - 1] < lst[i] and lst[i + 1] < lst[i]):
            return lst[i]

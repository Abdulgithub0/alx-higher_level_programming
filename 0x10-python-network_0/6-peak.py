#!/usr/bin/python3
"""a function that finds a peak in a list of unsorted integers."""


def find_peak(list_of_integers):
    """find peak function definition"""
    if list_of_integers:
        num = list_of_integers[0]
        for i in list_of_integers:
            if num < i:
                num = i
        return num
    return None

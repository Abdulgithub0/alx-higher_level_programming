#!/usr/bin/python3
"""a function that finds a peak in a list of unsorted integers."""


def find_peak(list_of_integers):
    """find peak function definition"""
    if list_of_integers:
        return sorted(list_of_integers)[-1]
    return None

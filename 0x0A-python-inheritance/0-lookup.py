#!/usr/bin/python3
"""lookup return a list of all methods and attributes in a class"""


def lookup(obj):
    """return dict

    Args:
        obj: any class instances
    Return: a list of methods and attributes in that instances
    """
    return (list(dir(obj)))

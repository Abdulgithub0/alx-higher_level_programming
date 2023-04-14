#!/usr/bin/python3
"""check for an exact instances"""


def is_same_class(obj, a_class):
    """working like type()

    Args:
        obj: obj to test for type/class
        a_class: class checking for
    Return: True if correct or false if otherwise
    """
    if (type(obj) == a_class):
        return True
    return False

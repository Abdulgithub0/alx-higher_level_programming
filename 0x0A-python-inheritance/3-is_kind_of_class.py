#!/usr/bin/python3
"""check for an exact or inherited instances"""


def is_kind_of_class(obj, a_class):
    """working like isinstance()

    Args:
        obj: obj to test for type/class
        a_class: class checking for
    Return: True if correct or false if otherwise
    """
    if (isinstance(obj, a_class)):
        return True
    return False

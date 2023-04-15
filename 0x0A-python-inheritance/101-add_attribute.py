#!/usr/bin/python3
"""adds a new attribute to an object if possible"""


def add_attr(obj, val, attr):
    """Add a new attribute to an object if it's possible."""
    if hasattr(obj, attr):
        setattr(obj, attr, val)
    else:
        raise TypeError("can't add new attribute")

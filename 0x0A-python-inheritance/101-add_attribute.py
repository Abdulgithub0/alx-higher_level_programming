#!/usr/bin/python3
"""adds a new attribute to an object if possible"""


def add_attribute(obj, attr, value):
    """Add a new attribute to an object if it's possible."""
    if hasattr(obj, "__dict__"):
        obj.__setattr__(attr, value)
    else:
        raise TypeError("can't add new attribute")

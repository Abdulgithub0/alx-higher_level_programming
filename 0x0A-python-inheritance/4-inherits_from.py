#!/usr/bin/python3
"""check for class instance"""

def inherits_from(obj, a_class):
    """check for obj or inheritances"""
    if (issubclass(type(obj), a_class) and type(obj) is not a_class):
        return True
    return False

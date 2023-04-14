#!/usr/bin/python3
"""check for class instance"""

def inherits_from(obj, a_class):
    """check for obj or inheritances"""
    if (isinstance(obj, a_class)):
        return True
    return False

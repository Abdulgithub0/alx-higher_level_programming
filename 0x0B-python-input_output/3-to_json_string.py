#!/usr/bin/python3
"""function that convert str to"""
import json


def to_json_string(my_obj):
    """return json representaion of my_obj

    Args:
        my_obj: string object
    """
    return (json.dumps(my_obj))

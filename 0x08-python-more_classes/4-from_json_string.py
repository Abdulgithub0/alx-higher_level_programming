#!/usr/bin/python3
"""function that return json rep"""
import json


def from_json_string(my_str):
    """return json representaion of my_obj

    Args:
        my_obj: string object
    """
    return (json.loads(my_str))

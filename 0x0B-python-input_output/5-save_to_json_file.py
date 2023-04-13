#!/usr/bin/python3
"""write object to text file using json representaion"""
import json


def save_to_json_file(my_obj, filename):
    """defining the the function

    Args:
        my_obj: object to be converted into json
        filename: path or name of the file to write into
    """
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(json.dumps(my_obj))

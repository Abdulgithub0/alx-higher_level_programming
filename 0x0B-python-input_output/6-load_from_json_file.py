#!/usr/bin/python3
""" function that creates an Object from a “JSON file”:"""
import json


def load_from_json_file(filename):
    """defining the the function

    Args:
        filename: path or name of the file to load json data from
    """
    with open(filename) as f:
        return json.load(f)

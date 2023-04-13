#!/usr/bin/python3
"""class to json"""


def class_to_json(obj):
    description = {}
    for key, value in obj.__dict__.items():
        if isinstance(value, (list, dict, str, int, bool)):
            description[key] = value
    return description

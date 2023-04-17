#!/usr/bin/python3
import json
"""Implementing Base class"""


class Base():
    """definition for Base class

    __nb_objects: private class instance
    """

    __nb_objects = 0

    def __init__(self, id=None):
        """initiazed the Base class

        Args:
            id: of each instances of Base
        """
        if not (id):
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """return json string
        Args:
            list_dictionaries: list of dictionaries
        """
        if (list_dictionaries and len(list_dictionaries) != 0):
            return json.dumps(list_dictionaries)
        return "[]"

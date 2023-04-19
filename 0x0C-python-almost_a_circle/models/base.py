#!/usr/bin/python3

"""
    implemented a class called Base that will serves
    as a superclass for all classes inside Almost a circle package
"""


import json


class Base:
    """
    This is the Base class, which provides a
    template for other classes to inherit from.

    Attributes:
        __nb_objects (int): A private class instance
        variable that keeps track of the number of Base objects created.

    Methods:
        __init__(self, id=None):
            Initializes a new instance of the
            Base class with an optional id parameter.
            If id is not provided, the id is set to None.
            Otherwise, a new id is assigned to the
            object using the private __nb_objects counter.
        to_json_string(list_dictionaries):
            Returns a JSON string representation of a list of dictionaries.

    """

    __nb_objects = 0

    def __init__(self, id=None):
        """
        Initializes a new instance of the
        Base class with an optional id parameter.
        If id is not provided, the id is set to None.
        Otherwise, a new id is assigned to the
        object using the private __nb_objects counter.

        Args:
            id (int): An optional parameter that
                      represents the id of the new instance.
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """
        Returns a JSON string representation of a list of dictionaries.

        Args:
            list_dictionaries (list): A list of
            dictionaries to be converted to a JSON string.

        Returns:
            str: A JSON string representation of the
            list of dictionaries. If the list is empty, returns '[]'.
        """
        if list_dictionaries and len(list_dictionaries) != 0:
            return json.dumps(list_dictionaries)
        return "[]"

    @classmethod
    def save_to_file(cls, list_objs):
        filename = cls.__name__
        filename += ".json"
        with open(filename, mode='w', encoding='utf-8') as f:
            store_dict = []
            if list_objs is not None:
                for obj in list_objs:
                    store_dict.append(dict(obj.to_dictionary()))
                store = cls.to_json_string(store_dict)
                f.write(store)
            else:
                f.write(str(store_dict))

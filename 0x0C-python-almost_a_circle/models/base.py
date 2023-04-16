#!/usr/bin/python3
"""Implementing Base class"""


class Base():
    """definition for Base class

    __nb_objects: private class instance
    """

    __nb_objects = 0

    def __init__(self, id=None):
        """initiazed the Base class"""
        if (id != None):
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

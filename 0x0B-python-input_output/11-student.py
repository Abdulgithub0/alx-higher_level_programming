#!/usr/bin/python3
"""creating student class"""


class Student:
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """return dict representation for the class"""
        if (type(attrs) == list):
            dic = {}
            d = self.__dict__
            for keys, val in d.items():
                if keys in attrs:
                    dic[keys] = val
            return dic
        else:
            return self.__dict__

    def reload_from_json(self, json):
        """replace stduent
        Args:
            json: dict obj to be used in replacement of cls attr
        """
        dic = self.__dict__
        for key, val in json.items():
            for k, v in dic.items():
                if key == k:
                    dic[key] = val

#!/usr/bin/python3
"""creating student class"""


class Student:
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        if (type(attrs) == list):
            dic = {}
            d = self.__dict__
            for keys, val in d.items():
                if keys in attrs:
                    dic[keys] = val
            return dic
        else:
            return self.__dict__

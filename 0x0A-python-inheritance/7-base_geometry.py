#!/usr/bin/python3
"""creating a class"""


class BaseGeometry():
    """implementing a BaseGeometry class"""
    def area(self):
        raise Exception('area() is not implemented')

    def integer_validator(self, name, value):
        """check the variable "value" validity"""
        if not (type(value) == int):
            raise TypeError(name + ' must be an integer')
        if value <= 0:
            raise ValueError(name + ' must be greater than 0')

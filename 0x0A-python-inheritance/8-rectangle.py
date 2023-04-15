#!/usr/bin/python3
"""creating a class"""


class BaseGeometry():
    """implementing a BaseGeometry class"""
    def __init__(self, width, height):
        integer_validator('width', width)
        self.__width = width
        integer_validator('height', height)
        self.__height = height

    def area(self):
        raise Exception('area() is not implemented')

    def integer_validator(self, name, value):
        """check the variable "value" validity"""
        if not (type(value) == int):
            raise TypeError(name + ' must be an integer')
        if value <= 0:
            raise ValueError(name + ' must be greater than 0')

#!/usr/bin/python3
BaseGeometry = __import__ ('7-base_geometry').BaseGeometry
"""creating a class"""


class Rectangle(BaseGeometry):
    """implementing a Rectangle class"""
    def __init__(self, width, height):
        super().integer_validator('width', width)
        self.__width = width
        super().integer_validator('height', height)
        self.__height = height

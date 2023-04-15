#!/usr/bin/python3
"""creating a class"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """implementing a Rectangle class"""
    def __init__(self, width, height):
        """initializing class Rectangle

        Args:
            width: width of rectangle in int type
            height: height of the reactangle in int type
        """
        self.integer_validator('width', width)
        self.__width = width
        self.integer_validator('height', height)
        self.__height = height

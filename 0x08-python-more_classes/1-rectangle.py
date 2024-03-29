#!/usr/bin/python3
"""definition for class Rectangle."""


class Rectangle:
    """ Class Rectangle data and method attributes."""

    def __init__(self, width=0, height=0):
        """ initialized the class instances with parameters

            args:
                width (int): the width of the rectange
                height (int): the height of the rectangle
        """

    @property
    def width(self):
        """getter method for class attribute width

            Return: width value
        """
        return self.__width

    @width.setter
    def width(self, value):
        """setter method for class attribute width

            args:
                value: new width value
        """
        if (isinstance(value, int)):
            if (value < 0):
                raise ValueError('width must be >= 0')
            self.__width = value
        else:
            raise TypeError('width must be an integer')

    @property
    def height(self):
        """getter method for class attribute height

            Return: height value
        """
        return self.__height

    @height.setter
    def height(self, value):
        """setter method for class attribute height

            args:
                value: new value for height attribute
        """
        if (isinstance(value, int)):
            if (value < 0):
                raise ValueError('height must be >= 0')
            self.__height = value
        else:
            raise TypeError('height must be an integer')

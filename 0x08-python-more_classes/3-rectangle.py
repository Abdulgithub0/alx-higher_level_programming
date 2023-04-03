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
        self.__width = width
        self.__height = height

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

    def area(self):
        """public method that compute the area of the for Class Rectangle"""
        return (self.__width * self.__height)

    def perimeter(self):
        """public attribute method that compute the perimeter
           for instances of cls Rectangle
        """
        if (self.__width == 0 or self.__height == 0):
            return 0
        return (2 * (self.__width + self.__height))

    def __str__(self):
        """ string representation for the Class Rectangle"""
        if (self.__width == 0 or self.height == 0):
            return ''
        for i in range(1, self.__height):
            print('#' * self.__width)
            if (i == self.__height - 1):
                return '#' * self.__width

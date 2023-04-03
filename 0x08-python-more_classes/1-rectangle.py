#!/usr/bin/python3
class Rectangle:

    def __init__(self, width=0, height=0):
        """ initialized the class instances with parameters

            args:
                width: the width of the rectange
                height: the height of the rectangle
        """

        if (isinstance(width, int)):
            if (width < 0):
                raise ValueError('width must be >= 0')
                self.__width = width
        else:
            raise TypeError('width must be an integer')

        if (isinstance(height, int)):
            if (height < 0):
                raise ValueError('height must be >= 0')
            self.__height = height
        else:
            raise TypeError('height must be an integer')

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

    def width(self):
        """getter method for class attribute width

            Return: width value
        """
        return self.__width

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

    def height(self):
        """getter method for class attribute height

            Return: width value
        """
        return self.__width

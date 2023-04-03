#!/usr/bin/python3
"""definition for class Rectangle."""


class Rectangle:
    """ Class Rectangle data and method attributes."""

    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """ initialized the class instances with parameters

            args:
                width (int): the width of the rectange
                height (int): the height of the rectangle
        """
        self.__width = width
        self.__height = height
        Rectangle.number_of_instances += 1

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
        if (self.__width == 0 or self.__height == 0):
            return ''
        s = str(self.print_symbol)
        return '\n'.join([s * self.__width for i in range(self.__height)])

    def __repr__(self):
        """create new string representation of the cls Rectangle"""
        return "Rectangle({},{})".format(self.__width, self.__height)

    def __del__(self):
        """method to delete any class instances when pass as arg to 'del'"""
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """check for equality"""

        if not (isinstance(rect_1, Rectangle)):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not (isinstance(rect_2, Rectangle)):
            raise TypeError('rect_2 must be an instance of Rectangle')
        if rect_1.area() >= rect_2.area():
            return rect_1
        return rect_2

    @classmethod
    def square(cls, size=0):
        """return a new rectangle instance with widht and height set to size"""

        cls.__width = size
        cls.__height = size
        return cls(cls.__width, cls.__height)

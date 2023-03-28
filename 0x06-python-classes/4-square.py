#!/usr/bin/python3
"""Creating a class square.
    self: reference the name of the object of instance 'Square'.
"""


class Square:
    """defining Class square body."""
    def __init__(self, __size=0):
        """
            Args:
                 __size: unaccessible/private field of the init method
        """
        if (isinstance(__size, int)):
            if (__size < 0):
                raise ValueError("size must be >= 0")
            self.__size = __size
        else:
            raise TypeError("size must be an integer")

    def area(self):
        """
           function area is a public method of class \
           Square that compute the area of the square.
        """
        return (self.__size * self. __size)

    def size(self, value):
        """
            setter method that change the value of private attribute __size.
        """
        if (isinstance(value, int)):
            if (value < 0):
                raise ValueError("size must be >=0")
            self.__size = value
        else:
            raise TypeError("size must be an integer")

    def size(self):
        """
            getter method  that return a copy of
            value of  private attribute __size.
        """
        return (self.__size)

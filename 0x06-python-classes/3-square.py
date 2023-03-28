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

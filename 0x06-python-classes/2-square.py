#!/usr/bin/python3
"""Creating a class square"""


class Square:
    """defining Class square body."""
    def __init__(self, __size=0):
        """
            self: refer to name of the class instance.

            Args:
                 __size: unaccessible/private field of the init method
        """
        if (isinstance(__size, int)):
            if (__size < 0):
                raise ValueError("size must be >= 0")
            self.__size = __size
        else:
            raise TypeError("size must be an integer")

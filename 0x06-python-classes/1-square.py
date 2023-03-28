#!/usr/bin/python3
"""Creating a class square"""


class Square:
    """defining Class square body."""
    def __init__(self, __size):
        """
            self: refer to name of the class instance.

            Args:
                 __size: size field of the square private to the class
        """
        self.__size = __size

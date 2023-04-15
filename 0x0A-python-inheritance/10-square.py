#!/usr/bin/python3
"""creating a class"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """implementing a Square class"""
    def __init__(self, size):
        """initializing class Square

        Args:
            size: size of the Square in int type
        """
        super().integer_validator('size', size)
        self.__size = size

    def area(self):
        """calculate the area of the Reactangle"""
        return self.__size * self.__size

    def __str__(self):
        """invoke call for print() and str()"""
        return '[Rectangle] {}/{}'.format(self.__size, self.__size)

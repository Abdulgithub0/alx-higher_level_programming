#!/usr/bin/python3
"""Creating a class square.
    self: reference the name of the object of instance 'Square'.
"""


class Square:
    """defining Class square body."""
    def __init__(self, __size=0, position=(0, 0)):
        """
            Args:
                 __size: unaccessible/private field of the init method
                position: is a tuple of two integers
        """
        if (isinstance(__size, int)):
            if (__size < 0):
                raise ValueError("size must be >= 0")
            self.__size = __size
        else:
            raise TypeError("size must be an integer")
        if ((type(position) == tuple) and (len(position) == 2)):
            self.__position = position
        else:
            raise TypeError("position must be a tuple of 2 positive integers")

    @property
    def position(self):
        return (self.__position)

    @position.setter
    def position(self, value):
        if ((type(position) == tuple) and (len(position) == 2)):
            self.__position = value
        else:
            raise TypeError("position must be a tuple of 2 positive integers")

    @property
    def size(self):
        """
            getter method  that return a copy of
            value of  private attribute __size.
        """
        return (self.__size)

    @size.setter
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

    def area(self):
        """
            function area is a public method of class \
            Square that compute the area of the square.
        """
        return (self.__size * self. __size)

    def my_print(self):
        """
            function that prints in stdout the square with the character '#'
        """
        if self.__size == 0:
            print()
        else:
            if (self.__position[1] > 0):
                print()
            for i in range(self.__size):
                print((' ' * self.__position[0]) + ('#' * self.__size))

    def __str__(self):
        if self.__size == 0:
            print()
        else:
            for j in range(self.__size):
                print((' ' * self.__position[0]) + ('#' * self.__size))
                if (j == self.__size - 1):
                    return ' ' * self.__position[0] + '#' * self.__size

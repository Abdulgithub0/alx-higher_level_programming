#!/usr/bin/python3
from models.base import Base
"""class Rectangle inherit from the Base class"""


class Rectangle(Base):
    """implement Rectangle class"""
    def __init__(self, width, height, x=0, y=0, id=None):
        """self.width(width)
        self.height(height)
        self.x(x)
        self.y(y)"""
        super().__init__(id)

        @property
        def width(self):
            return self.__width

        @width.setter
        def width(self, new_w):
            if (type(new_w) != int):
                raise TypeError('width must be an integer')
            if (new_w <= 0):
                raise ValueError('width must be > 0')
            self.__width = width

        @property
        def height(self):
            return self.__height

        @height.setter
        def height(self, new_height):
            if (type(new_height) != int):
                raise TypeError('height must be an integer')
            if (new_height <= 0):
                raise ValueError('height must be > 0')
            self.__height = height

        @property
        def x(self):
            return self.__width

        @x.setter
        def x(self, new_x):
            if (type(new_x) != int):
                raise TypeError('x must be an integer')
            if (new_x < 0):
                raise ValueError('x must be >= 0')
            self.__x = x

        @property
        def y(self, y):
            return self.__y

        @y.setter
        def y(self, new_y):
            if (type(new_y) != int):
                raise TypeError('y must be an integer')
            if (new_y < 0):
                raise ValueError('y must be >= 0')
            self.__y = y

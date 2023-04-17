#!/usr/bin/python3
from models.base import Base
"""class Rectangle inherit from the Base class"""


class Rectangle(Base):
    """implement Rectangle class"""
    def __init__(self, width, height, x=0, y=0, id=None):
        self.width = width
        self.height = height
        self.x = x
        self.y = y
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
        self.__width = new_w

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, new_height):
        if (type(new_height) != int):
            raise TypeError('height must be an integer')
        if (new_height <= 0):
            raise ValueError('height must be > 0')
        self.__height = new_height

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, new_x):
        if (type(new_x) != int):
            raise TypeError('x must be an integer')
        if (new_x < 0):
            raise ValueError('x must be >= 0')
        self.__x = new_x

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, new_y):
        if (type(new_y) != int):
            raise TypeError('y must be an integer')
        if (new_y < 0):
            raise ValueError('y must be >= 0')
        self.__y = new_y

    def area(self):
        return (self.__height * self.__width)

    def display(self):
        if (self.__width == 0 or self.__height == 0):
            print('')
            return
        for y in range(self.__y):
            print("")
        for j in range(self.height):
            print(" " * self.x, end='')
            print('#' * self.width, end='')
            print()

    def __str__(self):
        return "[Rectangle] ({}) {}/{} - {}/{}".format(self.id, self.__x,
                                                       self.__y, self.__width,
                                                       self.__height)

    def update(self, *args, **kwargs):
        if (len(args) != 0 and args[0]):
            for i in range(len(args)):
                match i:
                    case 0:
                        if (args[i] == None):
                            self.__init__(self.width, self.height, self.x, self.y)
                        else:
                            self.id = args[i]
                    case 1:
                        self.width = args[i]
                    case 2:
                        self.height = args[i]
                    case 3:
                        self.x = args[i]
                    case 4:
                        self.y = args[i]
        else:
            for keys, vals in kwargs.items():
                match keys:
                    case 'width':
                        self.width = vals
                    case 'height':
                        self.height = vals
                    case 'id':
                        self.id = vals
                    case 'x':
                        self.x = vals
                    case 'y':
                        self.y = vals

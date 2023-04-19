#!/usr/bin/python3

"""
    implementing class Rectangle that
    inherit from a class called Base
"""


from models.base import Base


class Rectangle(Base):
    """A class representing a rectangle.
    Constructs a new Rectangle object.

    Parameters:
        width (int): The width of the rectangle.
        height (int): The height of the rectangle.
        x (int): The x-coordinate of the top-left corner of the rectangle.
        y (int): The y-coordinate of the top-left corner of the rectangle.
        id (int): The ID of the rectangle.

    Raises:
        TypeError: If width, height, x, or y is not an integer.
        ValueError: If width, height, x, or y is less than or equal to 0.
    """

    def __init__(self, width, height, x=0, y=0, id=None):
        """initialize the class instances"""
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        """Get the width of the rectangle."""
        return self.__width

    @width.setter
    def width(self, new_w):
        """Set the width of the rectangle."""
        if type(new_w) != int:
            raise TypeError('width must be an integer')
        if new_w <= 0:
            raise ValueError('width must be > 0')
        self.__width = new_w

    @property
    def height(self):
        """Get the height of the rectangle."""
        return self.__height

    @height.setter
    def height(self, new_height):
        """Set the height of the rectangle."""
        if type(new_height) != int:
            raise TypeError('height must be an integer')
        if new_height <= 0:
            raise ValueError('height must be > 0')
        self.__height = new_height

    @property
    def x(self):
        """Get the x-coordinate of the rectangle."""
        return self.__x

    @x.setter
    def x(self, new_x):
        """Set the x-coordinate of the rectangle."""
        if type(new_x) != int:
            raise TypeError('x must be an integer')
        if new_x < 0:
            raise ValueError('x must be >= 0')
        self.__x = new_x

    @property
    def y(self):
        """Get the y-coordinate of the rectangle."""
        return self.__y

    @y.setter
    def y(self, new_y):
        """Set the y-coordinate of the rectangle."""
        if type(new_y) != int:
            raise TypeError('y must be an integer')
        if new_y < 0:
            raise ValueError('y must be >= 0')
        self.__y = new_y

    def area(self):
        """Calculate the area of the rectangle."""
        return (self.__height * self.__width)

    def display(self):
        """
        Print a representation of the rectangle to the console.
        If the rectangle has zero width or height, an empty line is printed.
        """
        if self.__width == 0 or self.__height == 0:
            print('')
            return
        for y in range(self.__y):
            print("")
        for j in range(self.height):
            print(" " * self.x, end='')
            print('#' * self.width, end='')
            print()

    def __str__(self):
        """Return a string representation of the rectangle."""
        return "[Rectangle] ({}) {}/{} - {}/{}".format(self.id, self.__x,
                                                       self.__y, self.__width,
                                                       self.__height)

    def area(self):
        """return the area of the rectangle"""
        return (self.__height * self.__width)

    def display(self):
        """print out the rectangle using paramters and cordinates"""
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
        """response to print() or str() calls on any instances of class"""
        return "[Rectangle] ({}) {}/{} - {}/{}".format(self.id, self.__x,
                                                       self.__y, self.__width,
                                                       self.__height)

    def update(self, *args, **kwargs):
        """an updater for the class parameter value"""
        if (len(args) != 0 and args):
            for i in range(len(args)):
                match i:
                    case 0:
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

    def to_dictionary(self):
        """return a dictionary of attributes for the class"""
        return {'width': self.width,
                'height': self.height,
                'id': self.id,
                'x': self.x,
                'y': self.y}

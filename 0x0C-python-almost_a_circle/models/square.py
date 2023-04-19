#!/usr/bin/python3

"""This module defines the Square class, a subclass of Rectangle"""


from models.rectangle import Rectangle


class Square(Rectangle):
    """"
    Classes:
        Square(Rectangle): Represents a square
                           with a size attribute and methods
        to manipulate it.

    Methods:
        __init__(self, size, x=0, y=0, id=None): Initializes a
                                                 new Square instance.
        size(self): Gets the value of the size attribute.
        size(self, new_val): Sets the value of the size attribute.
        __str__(self): Returns a string
                       representation of the Square instance.
        update(self, *args, **kwargs): Updates the attributes
                                       of the Square instance.
        to_dictionary(self): Returns the dictionary
                             representation of a Square instance.

    Attributes:
        All attributes from the Rectangle class are inherited, plus
        size (int): the size of the square.
    """

    def __init__(self, size, x=0, y=0, id=None):
        """Create a new Square instance with size"""
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """Get the value of the size attribute"""
        return self.width

    @size.setter
    def size(self, new_val):
        """Set the value of the size attribute to new_val"""
        self.width = new_val
        self.height = new_val

    def __str__(self):
        """Get a string representation of the Square instance"""
        return "[Square] ({}) {}/{} - {}".format(self.id,
                                                 self.x, self.y,
                                                 self.size)

    def update(self, *args, **kwargs):
        """
        Update the attributes of the Square
        instance using keyword/nonkeyword arguments
        """
        if (args and len(args) > 0):
            for i in range(len(args)):
                match i:
                    case 0:
                        self.id = args[i]
                    case 1:
                        self.size = args[i]
                    case 2:
                        self.x = args[i]
                    case 3:
                        self.y = args[i]
        else:
            for keys, vals in kwargs.items():
                match keys:
                    case 'id':
                        self.id = vals
                    case 'size':
                        self.size = vals
                    case 'x':
                        self.x = vals
                    case 'y':
                        self.y = vals

    def to_dictionary(self):
        """Get a dictionary representation of the Square instance"""
        return {'id': self.id, 'size': self.size, 'x': self.x, 'y': self.y}

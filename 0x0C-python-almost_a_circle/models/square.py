#!/usr/bin/python3
from models.rectangle import Rectangle
"""implementing class Square"""


class Square(Rectangle):
    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        return self.width

    @size.setter
    def size(self, new_val):
        self.width = new_val
        self.height = new_val

    def __str__(self):
        return "[Square] ({}) {}/{} - {}".format(self.id,
                                                 self.x, self.y,
                                                 self.size)

    def update(self, *args, **kwargs):
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
        return {'id': self.id, 'size': self.size, 'x': self.x, 'y': self.y}

#!/usr/bin/python3
"""define a square class"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """Square: inherit from rectangle class"""

    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(size, size, x, y, id)

    def __str__(self):
        return f"[Square] ({self.id}) {self.x}/{self.y} - {self.height}"

    @property
    def size(self):
        return self.height

    @size.setter
    def size(self, value):
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """square update"""
        a = len(args)
        if args is not None and a != 0:
            if a == 1:
                self.id = args[0]
            if a == 2:
                self.id = args[0]
                self.size = args[1]
            if a == 3:
                self.id = args[0]
                self.size = args[1]
                self.x = args[2]
            if a == 4:
                self.id = args[0]
                self.size = args[1]
                self.x = args[2]
                self.y = args[3]
        else:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        """Square instance to dictionary representation"""
        return {'id': getattr(self, 'id'),
                'size': getattr(self, 'width'),
                'x': getattr(self, 'x'),
                'y': getattr(self, 'y')}

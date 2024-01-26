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
        arg_list = ['id', 'size', 'x', 'y']
        if args is not None and len(args) != 0:
            for arg in args:
                setattr(self, arg_list[arg], args[arg])
        else:
            for key, value in kwargs.items():
                setattr(self, key, value)

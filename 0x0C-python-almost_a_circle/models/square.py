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
        return self.size

    @size.setter
    def size(Self, value):
        self.width = value
        self.height = height

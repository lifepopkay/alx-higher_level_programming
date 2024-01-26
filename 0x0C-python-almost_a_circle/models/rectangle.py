#!/usr/bin/python3
"""
    Rectangle: Inherit from Base
"""
from models.base import Base


class Rectangle(Base):
    """
        this rectangle inherit from Base class

        Args:
            width: the rectangle width
            height: the rectangle height
            x and y: other attributes of the rectangle
    """
    def __init__(self, width, height, x=0, y=0, id=None):
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    """
        the getter and setter for width, height, x and y
    """

    @property
    def width(self):
        """get the width"""
        return self.__width

    @width.setter
    def width(self, value):
        """set the width"""
        if value <= 0:
            raise ValueError("width must be > 0")
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        self.__width = value

    @property
    def height(self):
        """get the height"""
        return self.__height

    @height.setter
    def height(self, value):
        """set the height"""
        if value <= 0:
            raise ValueError("height must be > 0")
        if type(value) != int:
            raise TypeError("height must be an integer")
        self.__height = value

    @property
    def x(self):
        """set cordinates x"""
        return self.__x

    @x.setter
    def x(self, value):
        """set x"""
        if value < 0:
            raise ValueError("x must be > 0")
        if type(value) != int:
            raise TypeError("x must be an integer")
        self.__x = value

    @property
    def y(self):
        """get y"""
        return self.__y

    @y.setter
    def y(self, value):
        """set y"""
        if value < 0:
            raise ValueError("y must be >= 0")
        if type(value) != int:
            raise TypeError("y must be an integer")
        self.__y = value
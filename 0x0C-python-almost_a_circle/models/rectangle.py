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
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y

    """
        the getter and setter for width, height, x and y
    """

    @property
    def width(self):
        return self.__width
    @width.setter
    def width(self, value):
        self.__width = value

    @property
    def height(self):
        return self.__height
    
    @height.setter
    def height(self, value):
        self.__height = value

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, value):
        self.__x = value

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, value)
        self.__y = value

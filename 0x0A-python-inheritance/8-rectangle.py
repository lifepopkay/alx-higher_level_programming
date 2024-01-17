#!/usr/bin/python3
"""
   8-rectangle: class rectangle inherits from baseGeometry

"""


class Rectangle(BaseGeometry):

    def __init__(self, width, height):
        """
            initialises the attributes

            Args:
                    Width: the rectangle breadth
                    height: the rectangle length
        """
        self.integer_validator("width", width)
        self.integer_validator("height", height)

        self.__width = width
        self.__height = height

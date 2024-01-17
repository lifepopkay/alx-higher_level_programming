#!/usr/bin/python3

"""
	9-rectangle: Gives the full rectangle
"""

BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):

    def __init__(self, width, height):
        """
            initialises the attributes

            Args:
                    Width: the rectangle breadth
                    height: the rectangle length
        """
        super().integer_validator("width", width)
        super().integer_validator("height", height)

        self.__width = width
        self.__height = height

    def area(self):
        """
            This imple,ent the area of a rectangle
        """
        return (self.__height * self.__width)

   def __str__(self):
	"""
	   Return the print() and the Str() representation of a REctangle
	"""
	 return "[Rectangle] {}/{}".format(self.__width, self.__height)

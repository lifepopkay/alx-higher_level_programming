#!/usr/bin/python3

"""
This module is composed by a class that defines a Rectangle

"""

class Rectangle():
    """
         Additional argument to first class created

    """

    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        """
            This returns width

        """
        return self.__width

    @width.setter
    def width(self, value):
        """
            this define width

            Raise:
                TypeError if not integer
                ValueError if less than 0

        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must e >=0")
        self.__width = value

    @property
    def height(self):
        """
            This returns height

        """
        return self.__height

    @height.setter
    def height(self, value):
        """
            This defines height

            Raise:
                TypeError if height is not an integer
                ValueError if height is less than 0

        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")

        self.__height = value

    def area(self):
        """
            prints area of a rectangle

        """

        return (self.height * self.width)

    def perimeter(self):
        """
            prints perimeter of a rectangle

        """
        if self.width == 0 or self.height == 0:
            return 0
        return 2 * (self.width + self.height)

    def __str__(self):
        """
            print the rectangle with the character #

        """
        if self.width == 0 or self.height == 0:
            return ""

        rec = ""
        for i in range(self.height):
            rec += (str(print_symbol * self.width) + "\n"

        return rec[:-1]

    def __repr__(self):
        """
            Method return a string representation of the rectangle

        """
        return "Rectangle({:d}, {:d})".format(self.width, self.height)

    def __del__(self):
        """
            Print the message when an instance of Rectangle is deleted

        """
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """
            method that returns the large rectangle

            Args:
                rect_1: Reactangle 1
                rect_2: Reactangle 2

            Raise:
                TypeError: when some argument passed is not
                 an instance of the Rectangle class

                Returns:
                    the largest/bigger Rectangle

        """

        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")

        if rect_1.area() >= rect_2.area():
            return rect_1
        return rect_2

    @classmethod
    def square(cls, size=0):
        """
            Method that returns a new instance of rectangle

            Args:
                cls: Rectangle class
                size: rectangle width and height

            returns:
                a new instance of rectanle class
        """
        return cls(size, size)

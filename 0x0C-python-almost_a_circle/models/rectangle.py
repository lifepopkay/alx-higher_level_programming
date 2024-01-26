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
        if type(value) != int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """get the height"""
        return self.__height

    @height.setter
    def height(self, value):
        """set the height"""
        if type(value) != int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """set cordinates x"""
        return self.__x

    @x.setter
    def x(self, value):
        """set x"""
        if type(value) != int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """get y"""
        return self.__y

    @y.setter
    def y(self, value):
        """set y"""
        if type(value) != int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """Gives the shape's area"""
        return self.__width * self.height

    def display(self):
        """display #"""
        if self.__width <= 0 or self.__height <= 0:
            print("")

        print('\n' * self.y, end='')
        for i in range(self.__height):
            print(' ' * self.x + "#" * self.__width)

    def __str__(self):
        return "[Rectangle] ({}) {}/{} - {}/{}".format(self.id, self.x,
                                                       self.y, self.width,
                                                       self.height)

    def update(self, *args, **kwargs):
        """
            update the rectangle

            Args:
                *args(ints): New attribute values.
                - 1st argument represents id attribute
                - 2nd argument represents width attribute
                - 3rd argument represent height attribute
                - 4tth argument represents x attribute
                - 5th argument represents y attribute
                **kwargs (dict): New key/value pairs of attributes.
        """
        if args is not None and len(args) is not 0:
            if len(args) == 1:
                self.id = args[0]
            elif len(args) == 2:
                self.id = args[0]
                self.width = args[1]
            elif len(args) == 3:
                self.id = args[0]
                self.width = args[1]
                self.height = args[2]
            elif len(args) == 4:
                self.id = args[0]
                self.width = args[1]
                self.height = args[2]
                self.x = args[3]
            elif len(args) == 5:
                self.id = args[0]
                self.width = args[1]
                self.height = args[2]
                self.x = args[3]
                self.y = args[4]
        else:
            for key, value in kwargs.items():
                if key == 'id':
                    self.id = kwargs.get('id')
                elif key == 'height':
                    self.height = kwargs.get('height')
                elif key == 'width':
                    self.width = kwargs.get('width')
                elif key == 'x':
                    self.x = kwargs.get('x')
                elif key == 'y':
                    self.y = kwargs.get('y')

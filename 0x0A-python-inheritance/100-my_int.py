#!/usr/bin/python3

""" Myint: reverse operation """


class MyInt(int):
    """
        MyInt- class MyInt that inherits from int

        Return:
                == and != operators inverted
    """
    def __init__(self, value):
        self.value = value

    def __eq__(self, number):
        """ check if equal to and reverse """
        return self.value != number

    def __ne__(self, number):
        """ check if not equals to and reverse """
        return self.value == number

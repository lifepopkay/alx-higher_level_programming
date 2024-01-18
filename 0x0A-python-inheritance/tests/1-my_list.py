#!/usr/bin/python3
"""
    MyList: inherits from list

"""


class MyList(list):
    """
        This inherit from a list class

        Return:
                prints list in ascending order
    """

    def print_sorted(self):
        n = self.copy()
        n.sort()
        print(n)

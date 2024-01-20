#!/usr/bin/python3

"""
    2-append_write:  appends a string at the end of a text file
"""


def append_write(filename="", text=""):
    """
        Method: This append a  string at the end of a text file

        Args:
            filename: Name of file text
            text: string to append

        Returns:
            the number of characters added
    """
    with open(filename, 'a', encoding='UTF-8') as f:
        return f.write(text)

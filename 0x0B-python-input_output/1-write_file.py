#!/usr/bin/python3

"""
    1-write_file:  write a string to a text file
"""


def write_file(filename="", text=""):
    """
        Method: This write a string to a text file

        Args:
            filename: Name of file text
            text: string to write

        Returns:
            the number of characters written
    """
    with open(filename, 'w', encoding='UTF-8') as f:
        return f.write(text)

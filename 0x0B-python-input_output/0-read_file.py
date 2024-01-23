#!/usr/bin/python3
"""
    0-read_file: this read a text file
"""


def read_file(filename=""):
    """
        Function: reads a text file (UTF8) and prints it to stdout

        Args:
            filename: the name of the text file

        Return:
            Print the content of the file

    """
    with open(filename, encoding='UTF-8') as f:
        print(f.read(), end='')

#!/usr/bin/python3
"""
    100-append_after: inserts a line of text to a file.
"""


def append_after(filename="", search_string="", new_string=""):
    """
        Method: this insert a line of text to a file
                after a specfic string is found
        Args:
                Filename: Name of the file
                search_string: specific strong to search
                new_string: new string to be inserted
        Returns:
                file containing the text
    """
    with open(filename, 'a', encoding= 'utf-8') as f:
        for line in f.readline():
            if search_string in line:
                f.write(new_string)
            else:
                pass

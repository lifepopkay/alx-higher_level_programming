#!/usr/bin/python3
"""
    5-save_to_json_file:writes an Object to a text file using
    a JSON representation
"""
import json


def save_to_json_file(my_obj, filename):
    """
        Method: function write an object to a text file using json

        Args: my_obj - object to serailize
            filename: name of file

    """
    with open('filename', 'w', encoding='utf-8') as f:
        return json.dump(my_obj, f)

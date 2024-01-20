#!/usr/bin/python3
"""
    5-load_from_json_file:  creates an Object from a “JSON file
"""
import json


def load_from_json_file(filename):
    """
        Method: Write a function that creates an Object from a “JSON file

        Args: my_obj -filename: name of file to deserialize

    """
    with open('filename', 'r', encoding='utf-8') as f:
        json.load(f)

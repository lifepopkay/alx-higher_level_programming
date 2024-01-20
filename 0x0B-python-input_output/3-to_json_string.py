#!/usr/bin/python3

"""
    3-to_json_string: To JSON string
"""
import json


def to_json_string(my_obj):
    """
        Method: Function returns the JSON representation of an object

        Args:
            my_obj: a list or string or number

        Raises:
        Exception: when the objet can be encoded

    """
    return json.dumps(my_obj)

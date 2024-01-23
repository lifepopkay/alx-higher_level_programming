#!/usr/bin/python3

"""
    4-from_json_string: To JSON string
"""
import json


def from_json_string(my_obj):
    """
        Method: Function returns the object representation  of JSON string

        Args:
            my_obj:JSON a list or string or number

        Raises:
        Exception: when the objet can be decoded

    """
    return json.loads(my_obj)

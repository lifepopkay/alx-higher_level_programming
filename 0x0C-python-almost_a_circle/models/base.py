#!/usr/bin/python3
import json
"""
    Base: Base class of all other classes used
"""


class Base:
    """
        Base: base class for the project almost a circle

        private class attribute: _nb_objects = 0
    """
    __nb_objects = 0

    def __init__(self, id=None):
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """Dictionary to JSON string"""
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """Json string to file"""

        filename = f"{cls.__name__}.json"
        if list_objs is None:
            list_objs = []

        string = [obj.to_dictionary() for obj in list_objs]
        j_s = to_json_string(string)

        with open(filename, 'w', encoding='utf-8') as f:
            f.write(j_S)

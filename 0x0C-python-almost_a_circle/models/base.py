#!/usr/bin/python3
"""
    Base: Base class of all other classes used
"""
import json


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
        """save a json to file """

        if list_objs is None:
            list_objs = []

        s = [i.to_dictionary() for i in list_objs]
        s = cls.to_json_string(s)
        filename = f"{cls.__name__}.json"

        with open(filename, 'w', encoding='utf-8') as f:
            f.write(s)

    @staticmethod
    def from_json_string(json_string):
        """JSON string to dictionary"""
        if json_string is None or len(json_string) == 0 or json_string == []:
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """Create a dummy varaible that takes the dictionary"""
        dum_var = cls.__new__(cls)
        dum_var.__dict__.update(dictionary)

        return dum_var

    @classmethod
    def load_from_file(cls):
        """File to instances"""

        filename = f"{cls}.json"

        if not filename:
            return []
        else:
            with open(filename, 'r') as f:
                data = from_json_string(f)
                instance = []
                for i in data:
                    instance = cls.create(**i)
                    instance.append(instance)
                return instance

#!/usr/bin/python3
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
        if list_dictionaries is not None or list_dictionaries == []:
            return json.dumps(list_dictionaries)
        else:
            return []

    @classmethod
    def save_to_file(cls, list_objs):
        """Json string to file"""

        filename = f"{cls.__name__}.json"

        string = []
        if not list_objs:
            pass
        else:
            for line in range(len(list_objs)):
                string.append(list_objs[i].to_dictionary())

        l_d = cls.to_json_string(string)

        with open(filename, 'w') as f:
            f.write(l_d)

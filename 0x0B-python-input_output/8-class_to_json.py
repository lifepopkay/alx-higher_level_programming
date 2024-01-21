#!/usr/bin/python3
"""
    8-class_to_json: Class to JSON
"""


def class_to_json(obj):
   """
      function convert class attributes to json
      Args:
           obj: this instance of a class
      Return:
           Returns the dictionary description with simple data structure
    """
    return obj.__dict__    

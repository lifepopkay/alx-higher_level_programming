#!/usr/bin/python3

"""
    101-add_attribute: add_attribute()
"""


class add_attribute(obj, name, value):
    """
        Function that adds a new attribute to an object

        Args:
            Obj: object
            name: attribute name
            value: attribute value

        Raises:
                TypeError: when the attribute can't be added

    """
    if not hasattr(obj, '__dict__'):
        raise TypeError("can't add new attribute")
    setattr(obj, name, value)

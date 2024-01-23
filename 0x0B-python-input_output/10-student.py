#!/usr/bin/python3
"""
    Class Student
"""


class Student():
    """
        Method:
                Defines a students
    """
    def __init__(self,first_name, last_name, age):
        """
            initialize the attributes of the class

            Args:
                first_name: The student's first name
                last_name: THe student's last name
                age: THe student age
        """
        self.first_name= first_name
        self.last_name= last_name
        self.age= age

    def to_json(self, attrs=None):
        if (type(attrs) == list and
                all(type(i) == str for i in attrs)):
            return {key: getattr(self,key) for key in attrs if hasattr(self,key)}
        return self.__dict__

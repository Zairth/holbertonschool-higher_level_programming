#!/usr/bin/python3
"""My class Student"""


class Student():
    """My class Student"""

    def __init__(self, first_name, last_name, age):
        """My initialization"""

        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Function to convert into json format"""

        new_dict = {}

        if attrs is None:
            return self.__dict__

        for attr in attrs:
            if attr in self.__dict__:
                new_dict[attr] = self.__dict__[attr]

        return new_dict

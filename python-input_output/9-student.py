#!/usr/bin/python3
"""My class Student"""


class Student():
    """My class Student"""

    def __init__(self, first_name, last_name, age):
        """My initialization"""

        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """Function to convert into json format"""

        return self.__dict__

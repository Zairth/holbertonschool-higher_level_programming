#!/usr/bin/python3
"""task_01_pickle.py"""
import pickle


class CustomObject():
    """
    Create a new Instance
    """

    def __init__(self, name, age, is_student):
        """
        Init the Instance with public attributes
        """

        self.name = name
        self.age = age
        self.is_student = is_student

    def serialize(self, filename):
        """
        serialize the data into a filename using the pickle module
        """

        try:
            with open(filename, 'wb') as file:
                pickle.dump(self, file)

        except Exception as e:
            print("Error during serialization: {}".format(e))

            return None

    @classmethod
    def deserialize(cls, filename):
        """
        deserialize the data from a filename using the pickle module
        """

        try:
            with open(filename, 'rb') as file:
                data = pickle.load(file)

            return data

        except Exception as e:
            print("Error during deserialization: {}".format(e))

            return None

    def display(self):
        """
        print out the object’s attributes
        """

        print("Name: {}".format(self.name))
        print("Age: {}".format(self.age))
        print("Is Student: {}".format(self.is_student))

#!/usr/bin/python3
"""task_00_basic_serialization.py"""
import json


def serialize_and_save_to_file(data, filename):
    """writes an Object to a text file, using a JSON representation"""

    with open(filename, "w", encoding="utf-8") as file:
        file.write(json.dumps(data))


def load_and_deserialize(filename):
    """function that creates an Object from a “JSON file”"""

    with open(filename, "r", encoding="utf-8") as file:
        return json.load(file)

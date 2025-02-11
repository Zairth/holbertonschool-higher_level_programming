#!/usr/bin/python3
"""task_01_pickle.py"""
import csv
import json


def convert_csv_to_json(filename):
    """Convert csv into json"""

    try:
        new_data = []

        with open(filename, mode='r') as file:
            data = csv.DictReader(file)

            for row in data:
                new_data.append(row)

        with open("data.json", "w", encoding="utf-8") as file:
            json.dump(new_data, file)

        return True

    except Exception as e:
        print("Error during the conversion: {}".format(e))

        return False

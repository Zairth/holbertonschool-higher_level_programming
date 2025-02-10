#!/usr/bin/python3
"""adds all arguments to a Python list, and then save them to a file"""
import sys


load_from_json_file = __import__('6-load_from_json_file').load_from_json_file
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file

def add_items():
    """adds all arguments to a Python list, and then save them to a file"""

    filename = "add_item.json"

    try: 
        with open(filename, "r"):
            previous_content = load_from_json_file(filename)
            previous_content.extend(sys.argv[1:])
            save_to_json_file(previous_content, filename)
    except FileNotFoundError:
        items = sys.argv[1:]
        save_to_json_file(items, filename)

add_items()
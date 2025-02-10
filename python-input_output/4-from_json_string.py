#!/usr/bin/python3
"""Return a json string into Python data format"""
import json


def from_json_string(my_str):
    """Return a json string into Python data format"""

    return json.loads(my_str)

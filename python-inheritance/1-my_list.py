#!/usr/bin/python3
"""
Class to print a sorted list
"""


class MyList(list):
    """
    Create a new instance
    """

    def print_sorted(self):
        """Print a list in ascending order"""

        print(sorted(self))

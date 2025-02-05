#!/usr/bin/python3
"""1-my_list.py
"""


class MyList(list):
    """
    Create a new instance
    """

    def print_sorted(self):
        """Print a list in ascending order"""

        print(sorted(self))

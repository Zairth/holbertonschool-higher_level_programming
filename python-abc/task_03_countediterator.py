#!/usr/bin/python3


class CountedIterator:
    """New instance"""

    def __init__(self, iterator):
        """"Init new instance"""

        self.iterator = iter(iterator)
        self.count = 0

    def __next__(self):
        """Modify a built-in function"""

        new_elem = next(self.iterator)
        self.count += 1
        return new_elem
        if new_elem > len(new_elem):
            raise StopIteration

    def get_count(self):
        """Return the count"""

        return self.count

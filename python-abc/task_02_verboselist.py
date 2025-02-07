#!/usr/bin/python3


class VerboseList(list):
    """New Instance"""

    def append(self, element):
        """Adding functionnality to built-in functions"""

        super().append(element)
        print("Added [{}] to the list.".format(element))

    def extend(self, elem_added):
        """Adding functionnality to built-in functions"""

        count = len(elem_added)
        super().extend(elem_added)
        print("Extended the list with [{}] items.".format(count))

    def remove(self, element):
        """Adding functionnality to built-in functions"""

        super().remove(element)
        print("Removed [{}] from the list.".format(element))

    def pop(self, at_index=-1):
        """Adding functionnality to built-in functions"""

        element = super().pop(at_index)
        print("Popped [{}] from the list.".format(element))
        return element

#!/usr/bin/python3
def complex_delete(a_dictionary, value):

    for cle in list(a_dictionary.keys()):
        if a_dictionary[cle] == value:
            del a_dictionary[cle]

    return a_dictionary

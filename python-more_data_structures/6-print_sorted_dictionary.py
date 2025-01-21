#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    dictionary_sorted = dict()

    for keys in sorted(a_dictionary.keys()):
        dictionary_sorted[keys] = a_dictionary[keys]

    for key in dictionary_sorted:
        print("{}: {}".format(key, dictionary_sorted[key]))

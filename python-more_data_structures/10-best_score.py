#!/usr/bin/python3
def best_score(a_dictionary):
    best_value = ""
    max_integer = 0
    if a_dictionary is not None:
        for cle, valeur in a_dictionary.items():
            if a_dictionary[cle] > max_integer:
                max_integer = a_dictionary[cle]
                best_value = cle

        return best_value

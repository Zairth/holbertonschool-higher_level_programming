#!/usr/bin/python3
def best_score(a_dictionary):
    best_value = ""

    if not a_dictionary:
        return

    max_integer = 0

    for cle, valeur in a_dictionary.items():
        if valeur > max_integer:
            max_integer = valeur
            best_value = cle

    return best_value

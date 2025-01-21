#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary is not None:
        first_key = list(a_dictionary.keys())[0]
        max_integer = a_dictionary[first_key]
        best_value = first_key

        for cle, valeur in a_dictionary.items():
            if valeur > max_integer:
                max_integer = valeur
                best_value = cle

        return best_value
    return None

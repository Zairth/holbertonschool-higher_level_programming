#!/usr/bin/python3
def uniq_add(my_list=[]):
    my_set = set()
    result = 0

    for integers in my_list:
        my_set.add(integers)

    new_array = list(my_set)

    result = sum(new_array)

    return result

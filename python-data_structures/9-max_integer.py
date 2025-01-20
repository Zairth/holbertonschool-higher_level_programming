#!/usr/bin/python3
def max_integer(my_list=[]):
    if len(my_list) == 0:
        return None

    max = 0

    for integers in my_list:
        if integers > max:
            max = integers

    return max

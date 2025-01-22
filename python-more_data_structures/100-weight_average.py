#!/usr/bin/python3
def weight_average(my_list=[]):
    if len(my_list) == 0:
        return 0

    average = 0
    total = 0
    nb_to_divide = 0

    for tuple in my_list:
        total += tuple[0] * tuple[1]
        nb_to_divide += tuple[1]

    average = total / nb_to_divide

    return average

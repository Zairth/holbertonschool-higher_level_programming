#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    try:
        time_print = 0
        for i in range(x):
            print("{}".format(my_list[i]), end="")
            time_print += 1
    except IndexError:
        print("", end="")
    print("")
    return time_print

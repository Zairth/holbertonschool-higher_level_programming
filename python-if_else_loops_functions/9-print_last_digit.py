#!/usr/bin/python3

def print_last_digit(number):
    str_number = str(number)
    last_digit = str_number[-1]
    print("{}".format(last_digit), end="")
    return last_digit

#!/usr/bin/python3
def safe_print_integer_err(value):
    try:
        print("{:d}".format(value))
        return True
    except ValueError as err_msg:
        print("Exception: {}".format(err_msg))
        return False

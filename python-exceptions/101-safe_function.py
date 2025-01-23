#!/usr/bin/python3
import sys


def safe_function(fct, *args):
    try:
        result = fct(*args)
        return result
    except TypeError as err_msg:
        print("Exception: {}".format(err_msg), file=sys.stderr)
    except ValueError as err_msg:
        print("Exception: {}".format(err_msg), file=sys.stderr)
    except ZeroDivisionError as err_msg:
        print("Exception: {}".format(err_msg), file=sys.stderr)
    except IndexError as err_msg:
        print("Exception: {}".format(err_msg), file=sys.stderr)
    return None

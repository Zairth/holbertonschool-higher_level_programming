#!/usr/bin/python3
def delete_at(my_list=[], idx=0):

    if len(my_list) >= idx + 1 and idx >= 0:
        my_list.remove(idx + 1)

    return my_list

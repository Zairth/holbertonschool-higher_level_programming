#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    nw_tuple_a = [0, 0]
    nw_tuple_b = [0, 0]
    new_tuple = ()

    for i in range(2):
        if len(tuple_a) - 1 < i:
            nw_tuple_a[i] = 0
        else:
            nw_tuple_a[i] = tuple_a[i]
        if len(tuple_b) - 1 < i:
            nw_tuple_b[i] = 0
        else:
            nw_tuple_b[i] = tuple_b[i]

    new_tuple = nw_tuple_a[0] + nw_tuple_b[0], nw_tuple_a[1] + nw_tuple_b[1]

    return new_tuple

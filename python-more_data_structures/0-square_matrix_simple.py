#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    new_matrix = [lists[:] for lists in matrix]

    for lists in new_matrix:
        for i in range(len(lists)):
            lists[i] = lists[i] * lists[i]

    return new_matrix

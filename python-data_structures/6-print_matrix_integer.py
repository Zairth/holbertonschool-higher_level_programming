#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for list in matrix:
        for integer in list:
            print("{:d}".format(integer), end=" ")
        print("\n", end="")

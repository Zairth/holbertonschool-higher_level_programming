#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for list in matrix:
        for i in range(len(list)):
            if i + 1 > len(list) - 1:
                print("{:d}".format(list[i]), end="")
            else:
                print("{:d}".format(list[i]), end=" ")
        print("\n", end="")

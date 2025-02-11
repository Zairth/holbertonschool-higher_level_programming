#!/usr/bin/python3
"""12-pascal_triangle.py"""


def pascal_triangle(n):
    """
    returns a list of lists of integers representing the Pascal’s triangle of n
    """

    my_list = list()

    if n <= 0:
        return my_list

    for i in range(n):
        sous_liste = [j for j in range(i + 1)]
        my_list.append(sous_liste)

    for i in range(n):
        for j in range(i + 1):

            if j == 0:
                my_list[i][j] = 1
            if j == i:
                my_list[i][j] = 1

            if i >= 2 and j != 0 and j != i:
                my_list[i][j] = my_list[i - 1][j - 1] + my_list[i - 1][j]

    return my_list

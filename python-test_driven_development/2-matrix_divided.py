#!/usr/bin/python3
"""
Diviser l'ensemble des valeur d'une matrice par un chiffre donné
"""


def matrix_divided(matrix, div):
    """
    Diviser une matrice par un int
    Args:
        matrix (list[list]): La matrice
        div (int, float): La division
    Returns:
        list[list]: La nouvelle matrice divisé
    Exemple:
        >>> matrix_divided([[1, 2, 3], [4, 5, 6]], 3)
        [[0.33, 0.67, 1.0], [1.33, 1.67, 2.0]]
    """

    if div == 0:
        raise ZeroDivisionError("division by zero")
    elif not isinstance(div, (int, float)):
        raise TypeError("div must be a number")

    if isinstance(matrix, list):

        new_matrix = [row[:] for row in matrix]
        the_len_norme = len(new_matrix[0])

        for i in range(len(new_matrix)):

            if the_len_norme != len(new_matrix[i]):
                raise TypeError("Each row of the matrix \
must have the same size")

            if not isinstance(new_matrix[i], list):
                raise TypeError("matrix must be a matrix \
(list of lists) of integers/floats")

            for j in range(len(new_matrix[i])):

                if isinstance(new_matrix[i][j], (int, float)):
                    new_matrix[i][j] = round(new_matrix[i][j] / div, 2)
                else:
                    raise TypeError("matrix must be a matrix \
(list of lists) of integers/floats")

    else:
        raise TypeError("matrix must be a matrix \
(list of lists) of integers/floats")

    return new_matrix

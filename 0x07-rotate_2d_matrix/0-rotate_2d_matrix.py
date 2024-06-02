#!/usr/bin/python3
"""
Script rotates a 2D matrix, 90 degrees clockwise.
"""


def rotate_2d_matrix(matrix):
    """
    Rotates a 2D matrix, 90 degrees clockwise.

    Paramters:
        matrix (list): A 2D matrix to be rotated.
    """
    for x, y in enumerate(zip(*reversed(matrix))):
        matrix[x] = list(y)

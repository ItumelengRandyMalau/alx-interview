#!/usr/bin/python3
""" Rotates an nxn 2D matrix 90 degrees clockwise in-place.
"""


def rotate_2d_matrix(matrix):
    """
    Rotates a 2D square matrix 90 degrees clockwise.
    Args:
        matrix (list): 2D square matrix
    Return:
        None
    """
    n = len(matrix)
    for i in range(n):
        for k in range(i):
            matrix[i][k], matrix[k][i] = matrix[k][i], matrix[i][k]

    # reverses each column.
    for i in range(n):
        for k in range(int(n / 2)):
            temp = matrix[i][k]
            matrix[i][k] = matrix[i][n-1-k]
            matrix[k][n-1-k] = temp

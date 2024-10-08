#!/usr/bin/python3
"""
Generates Pascal's Triangle up to the nth row.

Args:
    n (int): The number of rows in the triangle.

Returns:
    List[List[int]]: A list of lists representing Pascal's Triangle.
"""


def pascal_triangle(n):
    """
    Generates Pascal's Triangle up to the nth row.

    Args:
        n (int): The number of rows in the triangle.

    Returns:
        List[List[int]]: A list of lists representing Pascal's Triangle.
    """
    if n <= 0:
        return []  # Returns an empty list for non-positive n

    triangle = []  # Initializes an empty list to store the rows
    for i in range(n):
        row = [1] * (i + 1)  # Creates a new row with i+1 elements.
        for j in range(1, i):
            # Updates the middle elements of the current row
            row[j] = triangle[i - 1][j - 1] + triangle[i - 1][j]
        triangle.append(row)  # Adds the completed row to the triangle

    return triangle

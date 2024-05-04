#!/usr/bin/python3
"""
This script contains a function that returns a list of lists of integers
representing Pascal’s triangle up to n rows.
"""


def pascal_triangle(n):
    """
    Returns a list of lists of integers representing
    Pascal’s triangle up to n rows.

    Parameters:
        n (int): Number of rows for Pascal's triangle.

    Returns:
        List[List[int]]: A list of lists containing
        the elements of Pascal's Triangle.
    """
    if n <= 0:
        return []

    triangle_list = []

    for i in range(n):
        row = []
        for j in range(i + 1):
            if j == 0 or j == i:
                row.append(1)
            else:
                row.append(
                    triangle_list[i - 1][j - 1] + triangle_list[i - 1][j]
                )
        triangle_list.append(row)

    return triangle_list

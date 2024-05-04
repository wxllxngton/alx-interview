#!/usr/bin/python3
"""
Script calculates the fewest number of operations needed
to result in exactly n H characters in the file.
"""


def minOperations(n):
    """
    Returns the fewest number of operations needed
    to result in exactly n H characters in the file.

    Parameters:
        n (int): Number of 'H' characters.

    Returns:
        int: The fewest number of operations needed.
    """
    if n <= 0:
        return 0

    operations = 0
    current_chars = 1
    clipboard = 0

    while current_chars < n:
        if n % current_chars == 0:
            clipboard = current_chars
        current_chars += clipboard
        operations += 1

    if current_chars == n:
        return operations
    else:
        return 0

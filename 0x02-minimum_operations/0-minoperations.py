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

    next_char = "H"  # Initialize next character
    body = "H"  # Initialize body of characters
    operations = 0  # Initialize operation count

    while len(body) < n:
        if n % len(body) == 0:
            operations += 2
            next_char = body
            body += body
        else:
            operations += 1
            body += next_char

    if len(body) != n:  # Check if correct number of characters is reached
        return 0

    return operations

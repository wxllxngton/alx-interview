#!/usr/bin/python3
"""
Script that determines if a given data set
represents a valid UTF-8 encoding.
"""


def validUTF8(data):
    """
    Determines if a given data set represents a valid UTF-8 encoding.

    Parameters:
        data (list): The data set.

    Returns:
        bool: True if the data set represents a valid UTF-8 encoding,
        False otherwise.
    """
    # Variable to track the number of remaining bytes for the current character
    remaining_bytes = 0

    for byte in data:
        # If no remaining bytes, this is the start of a new character
        if remaining_bytes == 0:
            # Check how many bytes this character occupies
            if byte >> 7 == 0b0:  # 1-byte character
                remaining_bytes = 0
            elif byte >> 5 == 0b110:  # 2-byte character
                remaining_bytes = 1
            elif byte >> 4 == 0b1110:  # 3-byte character
                remaining_bytes = 2
            elif byte >> 3 == 0b11110:  # 4-byte character
                remaining_bytes = 3
            else:
                # Invalid start byte for UTF-8 character
                return False
        else:
            # If remaining_bytes > 0, this byte should be a continuation byte
            if byte >> 6 != 0b10:
                # Invalid continuation byte
                return False
            remaining_bytes -= 1

    # If after processing all bytes, remaining_bytes is still not zero, \
    # it means incomplete sequence
    return remaining_bytes == 0

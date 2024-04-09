#!/usr/bin/python3
"""
Script contains a method that determines if all the boxes
can be opened.
"""


def canUnlockAll(boxes):
    """
    Determines if all the boxes can be opened.

    Args:
        boxes (list): A list of lists representing the boxes and their keys.

    Returns:
        bool: True if all boxes can be opened, else False.
    """
    # Initialize a set to store unique key values
    keys = set()
    # Add the index of the first box as it's unlocked initially
    keys.add(0)

    # Initialize a set to keep track of visited boxes
    visited = set()

    # Function to recursively explore boxes
    def explore_box(box_index):
        # Check if the box index is out of bounds
        if box_index < 0 or box_index >= len(boxes):
            return
        visited.add(box_index)
        box = boxes[box_index]
        # Iterate through keys in the box
        for key in box:
            # If the key opens a box that hasn't been visited yet
            if key not in visited:
                keys.add(key)
                explore_box(key)

    # Start exploring boxes
    explore_box(0)

    # Check if all boxes have been visited
    return len(visited) == len(boxes)

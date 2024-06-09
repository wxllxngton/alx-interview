#!/usr/bin/python3
"""
Defines island_perimeter function that calculates
the perimeter of an island in a grid.
"""


def island_perimeter(grid):
    """
    Calculates the perimeter of an island in a grid.

    Args:
        grid (list of list of int): A 2D grid
        where 1 represents land and 0 represents water.

    Returns:
        int: The perimeter of the island.
    """
    perimeter = 0
    rows = len(grid)
    cols = len(grid[0]) if rows > 0 else 0

    for index_in_grid, row in enumerate(grid):
        for index_in_row, box in enumerate(row):
            if box == 1:
                # Check left neighbor
                if (
                    index_in_row == 0
                    or grid[index_in_grid][index_in_row - 1] == 0
                ):
                    perimeter += 1
                # Check right neighbor
                if (
                    index_in_row == cols - 1
                    or grid[index_in_grid][index_in_row + 1] == 0
                ):
                    perimeter += 1
                # Check top neighbor
                if (
                    index_in_grid == 0
                    or grid[index_in_grid - 1][index_in_row] == 0
                ):
                    perimeter += 1
                # Check bottom neighbor
                if (
                    index_in_grid == rows - 1
                    or grid[index_in_grid + 1][index_in_row] == 0
                ):
                    perimeter += 1

    return perimeter

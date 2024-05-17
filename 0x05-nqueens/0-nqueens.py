#!/usr/bin/python3
"""
N-Queens Problem Solver

This program solves the N-Queens problem,
which is the challenge of placing N non-attacking queens on an N×N chessboard.
"""

import sys


def backtrack(
    row, board_size, occupied_cols, occupied_pos_diag, occupied_neg_diag, board
):
    """
    Backtracking function to find all solutions to the N-Queens problem.

    Args:
        row (int): Current row being processed.
        board_size (int): Size of the chessboard.
        occupied_cols (set): Set of occupied columns.
        occupied_pos_diag (set): Set of occupied positive diagonals.
        occupied_neg_diag (set): Set of occupied negative diagonals.
        board (list): 2D list representing the chessboard.

    Returns:
        None. Prints every possible solution to the problem.
    """
    if row == board_size:
        solution = []
        for r in range(board_size):
            for c in range(board_size):
                if board[r][c] == 1:
                    solution.append([r, c])
        print(solution)
        return

    for col in range(board_size):
        if (
            col in occupied_cols
            or (row + col) in occupied_pos_diag
            or (row - col) in occupied_neg_diag
        ):
            continue

        occupied_cols.add(col)
        occupied_pos_diag.add(row + col)
        occupied_neg_diag.add(row - col)
        board[row][col] = 1

        backtrack(
            row + 1,
            board_size,
            occupied_cols,
            occupied_pos_diag,
            occupied_neg_diag,
            board,
        )

        occupied_cols.remove(col)
        occupied_pos_diag.remove(row + col)
        occupied_neg_diag.remove(row - col)
        board[row][col] = 0


def solve_nqueens(board_size):
    """
    Solves the N-Queens problem and prints all solutions.

    Args:
        board_size (int): Size of the chessboard.

    Returns:
        None.
    """
    occupied_cols = set()
    occupied_pos_diag = set()
    occupied_neg_diag = set()
    board = [[0] * board_size for _ in range(board_size)]

    backtrack(
        0,
        board_size,
        occupied_cols,
        occupied_pos_diag,
        occupied_neg_diag,
        board,
    )


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)
    try:
        n = int(sys.argv[1])
        if n < 4:
            print("N must be at least 4")
            sys.exit(1)
        solve_nqueens(n)
    except ValueError:
        print("N must be a number")
        sys.exit(1)

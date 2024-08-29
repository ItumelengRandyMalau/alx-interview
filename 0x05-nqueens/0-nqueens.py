#!/usr/bin/python3
"""
This script solves the N queens puzzle, which is the challenge of placing
N non-attacking queens on an N×N chessboard.
"""

import sys


def is_safe(board, row, col):
    """
    Check if a queen can be placed on board[row][col] without being attacked.

    Args:
        board (list): The current state of the chessboard.
        row (int): The row index to check.
        col (int): The column index to check.

    Returns:
        bool: True if it's safe to place the queen, False otherwise.
    """
    # Check this row on the left side
    for i in range(col):
        if board[row][i] == 1:
            return False

    # Check upper diagonal on the left side
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    # Check lower diagonal on the left side
    for i, j in zip(range(row, len(board), 1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    return True


def solve_nqueens(board, col, solutions):
    """
    Solve the N queens problem using backtracking.

    Args:
        board (list): The current state of the chessboard.
        col (int): The current column to place the queen.
        solutions (list): A list to store all possible solutions.

    Returns:
        bool: True if a solution is found, False otherwise.
    """
    # Base case: If all queens are placed
    if col >= len(board):
        solution = []
        for r in range(len(board)):
            for c in range(len(board)):
                if board[r][c] == 1:
                    solution.append([r, c])
        solutions.append(solution)
        return True

    # Consider this column and try placing a queen in all rows one by one
    for i in range(len(board)):
        if is_safe(board, i, col):
            # Place the queen
            board[i][col] = 1

            # Recur to place the rest of the queens
            solve_nqueens(board, col + 1, solutions)

            # Backtrack: Remove the queen
            board[i][col] = 0

    return False


def nqueens(N):
    """
    Initialize the chessboard and start solving the N queens problem.

    Args:
        N (int): The size of the chessboard (N×N).
    """
    board = [[0 for _ in range(N)] for _ in range(N)]
    solutions = []
    solve_nqueens(board, 0, solutions)
    for solution in solutions:
        print(solution)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    try:
        N = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)

    if N < 4:
        print("N must be at least 4")
        sys.exit(1)

    nqueens(N)

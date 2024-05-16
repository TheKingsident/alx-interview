#!/usr/bin/python3
""" 0x05. N Queens
"""

import sys


def is_safe(board, row, col, N):
    """ is_safe function
    """
    # Check if there is a queen in the same column
    for i in range(col):
        if board[i] == row or abs(board[i] - row) == abs(i - col):
            return False
    return True


def solve(board, col, N, solutions):
    """ solve function
    """
    if col == N:
        solutions.append([[i, board[i]] for i in range(N)])
        return

    for i in range(N):
        if is_safe(board, i, col, N):
            board[col] = i
            solve(board, col + 1, N, solutions)


def nqueens(N):
    """ nqueens function
    """
    if not N.isdigit():
        print("N must be a number")
        sys.exit(1)

    N = int(N)
    if N < 4:
        print("N must be at least 4")
        sys.exit(1)

    board = [-1] * N
    solutions = []
    solve(board, 0, N, solutions)

    for solution in solutions:
        print(solution)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: ./0-nqueens.py N")
        sys.exit(1)

    nqueens(sys.argv[1])

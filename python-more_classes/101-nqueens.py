#!/usr/bin/python3
"""Solves the N queens puzzle using backtracking."""

import sys


def print_usage_and_exit(msg, code=1):
    """Print message and exit program."""
    print(msg)
    sys.exit(code)


def parse_args():
    """Validate command line arguments."""
    if len(sys.argv) != 2:
        print_usage_and_exit("Usage: nqueens N")
    try:
        n = int(sys.argv[1])
    except ValueError:
        print_usage_and_exit("N must be a number")
    if n < 4:
        print_usage_and_exit("N must be at least 4")
    return n


def solve_nqueens(n, row, current_solution, solutions):
    """Recursively solve N queens using backtracking."""
    if row == n:
        solutions.append(list(current_solution))
        return

    for col in range(n):
        if is_safe(col, current_solution):
            current_solution.append([row, col])
            solve_nqueens(n, row + 1, current_solution, solutions)
            current_solution.pop()


def is_safe(col, current_solution):
    """Check if placing a queen at (current_row, col) is safe."""
    row = len(current_solution)
    for q_row, q_col in current_solution:
        if q_col == col or abs(q_col - col) == abs(q_row - row):
            return False
    return True


if __name__ == "__main__":
    n_val = parse_args()
    all_solutions = []
    solve_nqueens(n_val, 0, [], all_solutions)
    for sol in all_solutions:
        print(sol)

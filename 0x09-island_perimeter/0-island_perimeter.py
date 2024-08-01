#!/usr/bin/python3
"""
0-island_perimeter.py
"""


def island_perimeter(grid):
    """Function that returns the perimeter of the island described in grid"""
    rows = len(grid)
    columns = len(grid[0])
    perimeter = 0
    for r in range(rows):
        for c in range(columns):
            if grid[r][c] == 1:
                if r == 0 or grid[r - 1][c] == 0:
                    perimeter += 1
                if c == 0 or grid[r][c - 1] == 0:
                    perimeter += 1
                if r == len(grid) - 1 or grid[r + 1][c] == 0:
                    perimeter += 1
                if c == len(grid[r]) - 1 or grid[r][c + 1] == 0:
                    perimeter += 1
    return perimeter

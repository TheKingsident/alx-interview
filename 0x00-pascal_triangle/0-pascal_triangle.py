#!/usr/bin/python3
""""
Module that creates a Pascal triangle
"""

def pascal_triangle(n):
	"""
	Function that creates a Pascal traingle
	"""
	pascal_triangle = []

	for i in range(n):
		row = [None for _ in range(i + 1)]
		row [0], row [-1] = 1, 1

		for l in range(1, len(row) - 1):
			row[l] = pascal_triangle[i - 1][l - 1] + pascal_triangle[i - 1][l]

		pascal_triangle.append(row)

	return (pascal_triangle)

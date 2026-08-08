#!/usr/bin/python3
"""Module for dividing elements of a matrix."""


def matrix_divided(matrix, div):
    """Divides all elements of a matrix by div.

    Args:
        matrix: A list of lists of integers or floats.
        div: The number to divide by (int or float).

    Returns:
        A new matrix containing the results rounded to 2 decimal places.

    Raises:
        TypeError: If matrix is not a valid list of lists of numbers,
                   if rows differ in size, or if div is not a number.
        ZeroDivisionError: If div is zero.
    """
    if not isinstance(matrix, list) or not matrix or not all(isinstance(row, list) for row in matrix):
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
    
    for row in matrix:
        if not all(isinstance(el, (int, float)) for el in row):
            raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
            
    row_size = len(matrix[0])
    if not all(len(row) == row_size for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")
        
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
        
    if div == 0:
        raise ZeroDivisionError("division by zero")
        
    return [[round(el / div, 2) for el in row] for row in matrix]

#!/usr/bin/python3

def matrix_divided(matrix, div):
    """
    Divide all elements of a matrix by a number.

    Args:
        matrix (list of lists): A matrix containing integers or floats.
        div (int or float): The number to divide by.

    Returns:
        list of lists: A new matrix with elements divided by div (rounded to 2 decimal places).

    Raises:
        TypeError: If matrix is not a list of lists of integers/floats.
        TypeError: If each row of the matrix does not have the same size.
        TypeError: If div is not a number (integer or float).
        ZeroDivisionError: If div is equal to 0.
    """
    if not isinstance(matrix, list) or not all(isinstance(row, list) for row in matrix):
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")

    if not all(len(row) == len(matrix[0]) for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")

    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number (integer or float)")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    result_matrix = []
    for row in matrix:
        new_row = [round(item / div, 2) for item in row]
        result_matrix.append(new_row)

    return result_matrix

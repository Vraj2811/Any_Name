"""
This module provides functions for matrix operations such as
creating a matrix, multiplying it by a scalar, transposing it, 
and printing it.
"""

def create_matrix(rows, cols):
    """
    Create a matrix with the given number of rows and columns.
    Each element is the sum of its row and column indices, modulo 10.

    :param rows: Number of rows in the matrix
    :param cols: Number of columns in the matrix
    :return: A 2D list representing the matrix
    """
    return [[(i + j) % 10 for j in range(cols)] for i in range(rows)]

def scalar_multiply_matrix(matrix, scalar):
    """
    Multiply a matrix by a scalar.

    :param matrix: The matrix to be multiplied
    :param scalar: The scalar to multiply the matrix by
    :return: The resulting matrix after multiplication
    """
    rows = len(matrix)
    cols = len(matrix[0])
    result = [[0] * cols for _ in range(rows)]
    for i in range(rows):
        for j in range(cols):
            result[i][j] = matrix[i][j] * scalar
    return result

def transpose_matrix(matrix):
    """
    Transpose the given matrix.

    :param matrix: The matrix to be transposed
    :return: The transposed matrix
    """
    rows = len(matrix)
    cols = len(matrix[0])
    result = [[0] * rows for _ in range(cols)]
    for i in range(rows):
        for j in range(cols):
            result[j][i] = matrix[i][j]
    return result

def print_matrix(matrix):
    """
    Print the given matrix.

    :param matrix: The matrix to be printed
    """
    for row in matrix:
        print(row)

# Example usage:
A = create_matrix(3, 3)
B = create_matrix(3, 3)

print("Matrix A:")
print_matrix(A)
print()

print("Matrix B:")
print_matrix(B)
print()

E = scalar_multiply_matrix(A, 3)
print("Matrix A * 3:")
print_matrix(E)
print()

A_transposed = transpose_matrix(A)
print("Transpose of Matrix A:")
print_matrix(A_transposed)

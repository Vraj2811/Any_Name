def create_matrix(rows, cols):
    return [[(i + j) % 10 for j in range(cols)] for i in range(rows)]

def scalar_multiply_matrix(M, scalar):
    rows = len(M)
    cols = len(M[0])
    result = [[0] * cols for _ in range(rows)]
    for i in range(rows):
        for j in range(cols):
            result[i][j] = M[i][j] * scalar
    return result

def transpose_matrix(M):
    rows = len(M)
    cols = len(M[0])
    result = [[0] * rows for _ in range(cols)]
    for i in range(rows):
        for j in range(cols):
            result[j][i] = M[i][j]
    return result

def print_matrix(M):
    for row in M:
        print(row)

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

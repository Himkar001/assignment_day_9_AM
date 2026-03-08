# matrix_ops.py

# Matrix Addition
def matrix_add(A, B):
    result = []

    for i in range(len(A)):
        row = []
        for j in range(len(A[0])):
            row.append(A[i][j] + B[i][j])
        result.append(row)

    return result


# Matrix Transpose
def matrix_transpose(matrix):
    return [list(row) for row in zip(*matrix)]


# Matrix Multiplication
def matrix_multiply(A, B):

    if len(A[0]) != len(B):
        return "Matrix dimensions do not match"

    result = [
        [sum(a * b for a, b in zip(row_a, col_b))
        for col_b in zip(*B)]
        for row_a in A
    ]

    return result


# Test Matrices
a = [[1, 2], [3, 4]]
b = [[5, 6], [7, 8]]

print("Matrix Addition:")
print(matrix_add(a, b))

print("\nMatrix Transpose:")
print(matrix_transpose(a))

print("\nMatrix Multiplication:")
print(matrix_multiply(a, b))
def determinant(matrix):
    if len(matrix) == 1:
        return matrix[0][0]
    else:
        det = 0
        for i in range(len(matrix)):
            det += matrix[0][i] * (-1) ** i * \
                determinant([row[:i] + row[i+1:] for row in matrix[1:]])
        return det


matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

print(determinant(matrix))

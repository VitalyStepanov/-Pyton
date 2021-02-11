class Matrix:
    def __init__(self, matrix):
        self.matrix = matrix

    def __str__(self):
        return '\n'.join(map(str, self.matrix))

    def __add__(self, other):
        c = []
        for i in range(len(self.matrix)):
            c.append([])
            for j in range(len(self.matrix[0])):
                c[i].append(self.matrix[i][j] + other.matrix[i][j])
        return '\n'.join(map(str, c))


matrix_1 = Matrix([[31, 22], [37, 43], [51, 86]])
matrix_2 = Matrix([[31, 22], [37, 43], [51, 86]])
print(f"Matrix 1\n{matrix_1}\n{'-' * 20}")
print(f"Matrix 2\n{matrix_2}\n{'-' * 20}")
print(matrix_1 + matrix_2)

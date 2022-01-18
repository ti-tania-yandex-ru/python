class Matrix:
    def __init__(self, matrix):
        self.matrix = matrix

    def __str__(self):
        final_result = ""
        for item in self.matrix:
            result = ""
            for inner_item in item:
                result = f'{result}{inner_item} '
            final_result = f'{final_result}{result}\n'
        return final_result

    def __add__(self, other):
        final_matrix = self.matrix
        for i in range(len(self.matrix)):
            for j in range(len(self.matrix[i])):
                final_matrix[i][j] = self.matrix[i][j] + other.matrix[i][j]
        return final_matrix


lst1 = [1, 2, 3]
lst2 = [4, 5, 6]
lst3 = [7, 8, 9]
list_of_lists1 = [lst1, lst2, lst3]
print(list_of_lists1)

lst4 = [1, 1, 1]
lst5 = [1, 1, 1]
lst6 = [1, 1, 1]
list_of_lists2 = [lst4, lst5, lst6]
print(list_of_lists1)

matrix1 = Matrix(list_of_lists1)
print(matrix1)
matrix2 = Matrix(list_of_lists2)
print(matrix2)
result = matrix1 + matrix2
print(result)

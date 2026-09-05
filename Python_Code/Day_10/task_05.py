# matrix addition
matrix1 = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

matrix2 = [
    [9, 8, 7],
    [6, 5, 4],
    [3, 2, 1]
]

result = [
    [0, 0, 0],
    [0, 0, 0],
    [0, 0, 0]
]

for i in range(0, len(matrix1)):
    for j in range(0, len(matrix1)):
        result[i][j] = matrix1[i][j] + matrix2[i][j]
        


print(result)
        

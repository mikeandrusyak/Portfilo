from transpose_as_dict import transpose_as_dict
def mat_mul(matrix1, matrix2):
    if type(matrix1) == tuple and type(matrix2) == tuple and type(matrix1[-1]) == list:
        if matrix1[0] == matrix2[1]:
            output = []
            for i in range(0, len(matrix1[-1]), matrix1[1]):
                row = []
                for j in range(0, matrix2[1]):
                    element = 0
                    for element1,element2 in zip(matrix1[-1][i:i + 3],matrix2[-1][j::2]):
                        element += element1*element2
                    row.append(element)
                output.append(row)
            return (matrix1[0], matrix2[1], output)
        else:
            raise ValueError
    elif type(matrix1) == tuple and type(matrix2) == tuple and type(matrix1[-1]) == dict:
        rows1, cols1, values1 = matrix1
        rows2, cols2, values2 = matrix2

        if cols1 != rows2:
            raise ValueError

        output = (rows1, cols2, {})

        for (i, k1), v1 in values1.items():
            for (k2, j), v2 in values2.items():
                if k1 == k2:  # Сумісні елементи
                    if (i, j) not in output[2]:
                        output[2][(i, j)] = 0
                    output[2][(i, j)] += v1 * v2
        return output
    else:
        if len(matrix1)== len(matrix2[0]):
            transposed_matrix_2 = transpose_as_dict(matrix2)
            output = []
            for hight in range(len(matrix1)):
                row = []
                for lenth in range(len(matrix2[0])):
                    element = 0
                    for element1,element2 in zip(matrix1[hight],transposed_matrix_2[lenth]):
                        element += element1*element2
                    row.append(element)
                output.append(row)
            return output
        else:
            raise ValueError
print(mat_mul((2, 3, {(0, 0): 1, (0, 2): 3, (1, 1): 2, (1, 2): 4}),
              (3, 2, {(0, 0): 1, (1, 1): 2, (2, 0): 3, (2, 1): 4})))
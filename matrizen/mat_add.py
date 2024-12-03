def are_same_size(matrix1, matrix2):
    return len(matrix1) == len(matrix2) and all(len(row1) == len(row2) for row1, row2 in zip(matrix1, matrix2))


def mat_add(matrix1,matrix2):
    if type(matrix1) == tuple and type(matrix2) == tuple and type(matrix1[-1]) == list:
        if matrix1[0]!=matrix2[0] or matrix1[1] != matrix2[1]:
            raise ValueError
        else:
            output = []
            for element1, element2 in zip(matrix1[-1],matrix2[-1]):
                output.append(element1+element2)
            return(matrix1[0],matrix1[1], output)
    elif type(matrix1) == tuple and type(matrix2) == tuple and type(matrix1[-1]) == dict:
        if matrix1[0]!=matrix2[0] or matrix1[1] != matrix2[1]:
            raise ValueError
        else:
            output = matrix1[-1]
            for key, value in matrix2[-1].items():
                if key in output:
                    output[key] += value
                else:
                    output[key] = value
                if output[key] == 0:
                    del output[key]
            return(matrix1[0],matrix1[1], output)
    else:
        if are_same_size(matrix1, matrix2)== False:
            raise ValueError
        else:
            output = []
            for row1, row2 in zip(matrix1, matrix2):
                sum_in_row = []
                for element1, element2 in zip(row1, row2):
                    sum_in_row.append(element1+element2)
                output.append(sum_in_row)
            return output

print(mat_add((1,1,{(0,0):1}), (1,1,{(0,0):-1})))
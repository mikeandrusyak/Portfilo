
def as_dict(matrix):
    output = {}
    for row in range(len(matrix)):
        for col in range(len(matrix[row])):
            if matrix[row][col] != 0:
                output[(row, col)] = matrix[row][col] 
    return (len(matrix), len(matrix[0]), output)
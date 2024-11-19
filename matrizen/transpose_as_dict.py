from transpose_flatten import transpose_flatten as  transpose
from as_dict import as_dict
from flatten import flatten

def transpose_as_dict(matrix):
    if type(matrix) == tuple and type(matrix[2]) == dict:
        output = {}
        for key, value in matrix[2].items():
            output[(key[1],key[0])] = value
        return (matrix[1], matrix[0], output)
    else:
        return transpose(matrix)
    
matrix = [[1, 0, 3], [0, 2, 4]]

print(transpose_as_dict(matrix))
print(transpose_as_dict(flatten(matrix)))
print(transpose_as_dict(as_dict(matrix)))

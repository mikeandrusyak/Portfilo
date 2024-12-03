from datetime import datetime
def transpose(m):
    start = datetime.now()
    transpose_matrix = []

    for row in range(len(m[0])):
        new_line = []
        for column in range(len(m)):
            new_line.append(m[column][row])
        transpose_matrix.append(new_line)

    print('transpose: ', datetime.now()-start)
    return transpose_matrix

# print(transpose([[1, 0, 3], [0, 2, 4]]))
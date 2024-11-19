import transpose

def updated_transpose(m):
    if(type(m)) == tuple:
        un_flatten = []
        for coll in range(m[1]):
            un_flatten += m[2][coll::m[1]]
        return(m[1],m[0], un_flatten)
    else:
        return transpose.transpose(m)

print(updated_transpose((2, 3, [1, 0, 3, 0, 2, 4])))
print(updated_transpose((3, 2, [1, 0, 0, 2, 3, 4])))
print(updated_transpose([[1, 0, 3], [0, 2, 4]]))


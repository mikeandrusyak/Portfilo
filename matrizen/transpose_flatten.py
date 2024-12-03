import transpose

def transpose_flatten(m):
    if(type(m)) == tuple:
        un_flatten = []
        for coll in range(m[1]):
            un_flatten += m[2][coll::m[1]]
        return(m[1],m[0], un_flatten)
    else:
        return transpose.transpose(m)


def well_formed_matrix(lst):
    len_list = []
    for i in lst:
        len_list.append(len(i))

    if len(set(len_list)) == 1 and len_list[0] > 0:
        return True
    else:
        return False

print(well_formed_matrix([[1, 0], [0, 2], [3, 4]]))
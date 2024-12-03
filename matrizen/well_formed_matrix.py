from datetime import datetime

def well_formed_matrix_1(lst):
    start = datetime.now()
    len_list = []
    for i in lst:
        len_list.append(len(i))

    if len(set(len_list)) == 1 and len_list[0] > 0:
        print('well_formed_matrix_1: ', datetime.now()-start)
        return True
    else:
        print('well_formed_matrix_1: ', datetime.now()-start)
        return False

def well_formed_matrix_2(lst):
    start = datetime.now()
    if len(lst) == 0:
        print('well_formed_matrix_2: ', datetime.now()-start)
        return False
    else:
        len_first = len(lst[0])
    for i in range(1, len(lst)):
        if len(lst[i]) != len_first:
            print('well_formed_matrix_2: ', datetime.now()-start)
            return False
    if len_first == 0:
        print('well_formed_matrix_2: ', datetime.now()-start)
        return False
    else:
        print('well_formed_matrix_2: ', datetime.now()-start)
        return True
    

print(well_formed_matrix_1([]))
print(well_formed_matrix_2([]))
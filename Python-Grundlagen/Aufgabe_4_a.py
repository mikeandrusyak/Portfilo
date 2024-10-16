def rotate_left_str(s,n):
    lengh_s = len(s)
    rest = lengh_s % n
    return s[rest+1:]+s[:rest+1]

print(rotate_left_str('abcdefgh',3))
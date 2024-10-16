def move2_str(s):
    left_part = ''
    right_part = ''
    for i in range(len(s)):
        if i % 2 == 0:
            right_part += s[i]
        else:
            left_part += s[i]

    return left_part+right_part

print(move2_str('abcdefgh'))
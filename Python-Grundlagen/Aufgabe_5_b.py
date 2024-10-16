def str_count_any(string, pattern):
    count = 0
    for i in list(pattern):
        for j in string:
            if i == j:
                count+=1

    return count
print(str_count_any("Das ist ein netter Versuch", "er"))
def str_count(string, pattern):
    len_pattern = len(pattern)
    count = 0
    for i in range(len(string)-len_pattern):
        if string[i:i+len_pattern] == pattern:
            count +=1
    return count
print(str_count("Das ist ein netter Versuch","er"))
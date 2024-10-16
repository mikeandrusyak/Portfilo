def max_index(lst):
    max = 0
    for i in range(len(lst)-1):
        if lst[i+1]>lst[i]:
            max = i+1
    return max
print(max_index([-1,-5]))
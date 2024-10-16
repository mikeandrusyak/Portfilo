def mod5(N):
    output = []
    for i in range(N):
        if i**2 % 5 == 4:
            output.append(i)
    return output

print(mod5(20))
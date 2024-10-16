def kaprekar_konstante(num):
    if num < 10:
        num *= 1000
    elif num < 100:
        num *= 100
    elif num < 1000:
        num *= 10

    step = 0
    num_list = [digit for digit in str(num)]
    while int(''.join(sorted(num_list,reverse=True))) != 7641:
        num = int(''.join(sorted(num_list,reverse=True)))-int(''.join(sorted(num_list)))
        num_list = [digit for digit in str(num)]
        step +=1
        if step>100:
            return False, "more then 100 steps"
    return True, "on step: ", step


print(kaprekar_konstante(9273))
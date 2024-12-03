def is_prime(number):
    if number >1:
        for i in range(2, round(number**0,5+1)):
            print(i)
            if number % i == 0:
                return False
    return True

print(is_prime(41))

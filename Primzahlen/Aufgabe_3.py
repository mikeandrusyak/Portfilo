from datetime import datetime
def eratosthenes(n):
    start = datetime.now()
    list_with_numbers = list(range(2,n+1))
    prime_index = 0
    x = list_with_numbers[prime_index]
    while x*x<=n:
        i = 2
        while i * x <= n:
            try:
                list_with_numbers.remove(i * x)
            except ValueError:
                pass
            i += 1
        prime_index += 1
        x=list_with_numbers[prime_index]
    print('duration: eratosthenes', datetime.now()-start)
    return list_with_numbers
# print(eratosthenes(1000))


def eratosthenes_2(n):
    start = datetime.now()
    s = set(range(2, n + 1))
    x = 2
    while x * x<= n:
        # streiche alle Vielfachen von x aus der Liste
        if x in s:
            i = 2
            while i * x<= n:
                try:
                    s.remove(i * x)
                except KeyError:
                    pass
                i = i + 1
        x += 1
    print('duration eratosthenes_2: ', datetime.now()-start)
    return sorted(s)
# print(eratosthenes_2(1000))


def eratosthenes_3(n):
    start = datetime.now()
    s = set(range(2, n + 1))
    x = 2
    while x*x<= n:
        if x in s:
            # streiche alle Vielfachen von x aus der Liste
            s = s.difference(set(range(2 * x, n + 1, x)))
        x += 1
    print('duration eratosthenes_3: ', datetime.now()-start)
    return sorted(s)

print(eratosthenes_3(1000))
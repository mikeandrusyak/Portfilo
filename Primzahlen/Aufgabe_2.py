import Aufgabe_1
from datetime import datetime
def all_primes(number):
    start = datetime.now()
    is_primes = []
    for i in range(number+1):
        if Aufgabe_1.is_prime(i):
            is_primes.append(i)
    print('duration: ', datetime.now()-start)
    return is_primes

print(all_primes(97))
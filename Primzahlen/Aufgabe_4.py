from Aufgabe_3 import eratosthenes_3 as eratosthenes

def distances(n):
    prime_list = eratosthenes(n)
    distance = []
    for  i in range(len(prime_list)-1):
        distance.append(prime_list[i+1]-prime_list[i])
    return distance

print(distances(100))
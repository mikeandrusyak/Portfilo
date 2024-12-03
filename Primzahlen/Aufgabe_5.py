from Aufgabe_4 import distances

def heuristic(n):
    distance_list = distances(n)
    frequency = {}

    for d in distance_list:
        if d in frequency:
            frequency[d] += 1
        else:
            frequency[d] = 1

    copple = list(frequency.items())
    
    return copple

print(heuristic(100))
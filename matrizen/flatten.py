from datetime import datetime

def flatten(m):
    start = datetime.now()
    elements = []
    for i in m:
        elements += i
    print('transpose: ', datetime.now()-start)
    return (len(m), len(m[0]), elements)

print(flatten([[1, 0, 3], [0, 2, 4]]))
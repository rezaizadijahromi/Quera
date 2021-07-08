n = input()

def loknat(n):
    counter = 0
    for i in n:
        if i in ('T', 'D', 'F', 'L'):
            counter += 1
    return counter

print(2 ** loknat(n))

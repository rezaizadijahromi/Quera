n = int(input())
stack = []

def calc(n):
    sumation = 0
    for i in range(n):
        vorodi = int(input())
        sumation += vorodi
        stack.append(vorodi)

    mean = sumation / n

    return mean

def chideman(n):
    count = 0
    javab = 0
    n = n
    mean = calc(n)
    for i in stack:
        if i <= mean:
            count = mean - i
            javab += count

    return javab


print(int(chideman(n)))
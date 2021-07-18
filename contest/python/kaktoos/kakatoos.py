n = int(input())

def kaktoos(n):
    stack = list(map(int, input().split()))
    # print(stack)
    javab = ''
    for i in stack:
        if i > 3:
            print('*')
        else:
            for j in range(1, i+1):
               javab+= '*'
            print(javab)
            javab = ''

kaktoos(n)
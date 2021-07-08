def boostan():
    first = list(map(int, input().split()))
    second = list(map(int, input().split()))

    x1 = first[0]
    x2 = second[0]

    if x1 > x2:
        print('Left')
    else:
        print('Right')

boostan()
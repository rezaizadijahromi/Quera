def kharidar_nashi():
    satr,soton, break_keys = map(int, input().split())

    keys = list()
    cordinates = list()
    for i in range(satr):
        keys.append([i if int(i) in keys else 0 for i in range(soton)])

    for i in range(break_keys):
        x, y = map(int, input().split())
        keys[x-1][y-1] = 1
    data = (len(keys) * soton)
    javab = 0

    for i in range(satr):
        for j in range(soton):
            if keys[i][j] == 0:
                cordinates.append([i+1, j+1])


    if data > break_keys:
        if break_keys % 2 == 0:
            if break_keys > 0:
                javab = 1
            else:
                javab = 1
        else:
            if data == (break_keys + 1):
                javab = 0
    elif data == break_keys:
        javab = -1

    print(javab)
    for i in range(javab):
        print(*cordinates[i])


kharidar_nashi()
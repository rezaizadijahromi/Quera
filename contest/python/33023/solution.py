def peek_finder():
    p, q = map(int, input().split())

    jadval = [list(map(int, input().split())) for i in range(p)]

    counter = 0

    for i in range(1, p-1):
        for j in range(1, q-1):
            a1 = jadval[i][j] - jadval[i-1][j]
            a2 = jadval[i][j] - jadval[i+1][j]
            b1 = jadval[i][j] - jadval[i][j-1]
            b2 = jadval[i][j] - jadval[i][j+1]

            if a1 * a2 > 0 and b1 * b2 > 0 and a1 * b1 < 0:
                counter += 1
    return counter


print(peek_finder())


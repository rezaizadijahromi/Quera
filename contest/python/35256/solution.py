def sub():

    n, W = map(int, input().split())
    w = list(map(int, input().split()))
    maximum = 0
    for i in range(n):
        for j in range(i + 1, n + 1):
            a = sum(w[:j]) - sum(w[:i])
            if a <= W and  maximum < a:
                maximum = a
    return maximum

print(sub())
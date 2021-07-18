def sang_brande():
    n = int(input())
    mitavanad = False
    for i in range(1000):
        if n == 1:
            mitavanad = True
            break
        if n % 2 == 0:
            n /= 2
        else:
            n = n * 3
            n += 3

    if mitavanad:
        print('Yes')
    else:
        print('No')

sang_brande()
def sharger():
    n, x, y = list(map(int, input().split()))

    phones = list(map(int, input().split()))

    phones = sorted(phones)

    while phones[0] >= x:
        changed = False
        for i in range(1, n):
            if phones[i] < 100:
                phones[0] -= x
                phones[i] += y
                changed = True

        if changed == False:
            break

    for i in range(1, n):
        if phones[i] < 100:
            return "NO"      
        
    return "YES"


print(sharger())


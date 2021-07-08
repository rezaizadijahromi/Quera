def sucks(n):
    suc = list(map(int, input().split()))
    pairs = []
    counter = 0

    for i in range(0, len(suc)):
        for j in range(i+1, len(suc)):
            # print(suc[i], suc[j])
            if suc[i] == suc[j]:
                if i not in pairs and j not in pairs:
                    counter += 1
                    pairs.append(i)
                    pairs.append(j)
                    

    result = []
    pairs = [i+1 for i in pairs]
    for i in range(0, len(pairs), 2):
        result.append(pairs[i:i+2])

    # print(pairs)
    print(counter)
    for i in result:
        print(*i)



n = int(input())
sucks(n)
# print(sucks(n))
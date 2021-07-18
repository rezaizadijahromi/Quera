def free_time():

    n, m = list(map(int, input().split()))

    s = 0
    counter = 0
    words = [input() for i in range(n + 1)]
    words2 = list(map(list, zip(*words[:n])))
    for i in range(n):
        
        while words[n] in words[i]:

            s = words[i].index(words[n])
            words[i] = words[i].replace(words[i][s], '*', 1)

            counter += 1
    for i in range(m):
        words2[i] = ''.join(words2[i])
        while words[n] in words2[i]:
            s = words2[i].index(words[n])
            words2[i] = words2[i].replace(words2[i][s], '*', 1)

            counter += 1
            
    return counter


print(free_time())
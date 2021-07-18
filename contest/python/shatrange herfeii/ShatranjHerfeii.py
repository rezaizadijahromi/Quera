n = list(map(int, input().split()))

f = []

f.append((1 - n[0]))
f.append((1 - n[1]))
f.append((2 - n[2]))
f.append((2 - n[3]))
f.append((2 - n[4]))
f.append((8 - n[5]))

print(*f)
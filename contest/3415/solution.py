  
n = int(input())
p, q = zip(*[map(int, input().split()) for i in range(n)])

bdn = 0
for x in range(n):
    for y in range(n):
        if x != y:
            if p[x] >= p[y] and q[x] <= q[y]:
                bdn += 1
                break
print(n - bdn)
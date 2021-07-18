n = int(input())
l = list(map(int, input().split()))

l.reverse()

r = 0
for i in l:
    r += i
    if r < 0:
        r = 0

if r < 0:
    print(0)
else:
    print(r)
n, k = list(map(int, input().split()))

a = 0
for i in range(0, n):
    a += int(input())

if a >= k:
    print("YES")
else:
    print("NO")
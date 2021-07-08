n, k = list(map(int, input().split()))


x = k
i = 1
x = x %n
while x != 0:
    i += 1
    x += k
    x = x % n

print(i)
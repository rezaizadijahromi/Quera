a, b, l = list(map(int, input().split()))

num = 0
count = 0
i = True
while i:

    if count != l:
        num += a
        count += 1
    if count != l:
        num += b
        count += 1

    else:
        break

print(num)
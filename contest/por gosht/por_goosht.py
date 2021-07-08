n, m = list(map(int, input().split()))

b1 = 0
b2 = 0
for i in range(2*(n)):
    gosht = input()
    if i < n:
        b1 += gosht.count('*')
    else:
        b2 += gosht.count('*')

print(b1, b2)

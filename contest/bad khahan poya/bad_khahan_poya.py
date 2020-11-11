x, y = map(int, input().split())

c = 0
r = -1 

while r < 0 or r > x/2:
    c += 1
    result = y*c
    r = result % x


print(result)
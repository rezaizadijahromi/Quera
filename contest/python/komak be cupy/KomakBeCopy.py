x = list(map(str, input().split()))

n = int(x[0])
s = ""
for i in range(n):
    s += "copy of "

print(s + x[1])
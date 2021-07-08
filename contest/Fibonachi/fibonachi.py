n = int(input())

f0 = 0
f1 = 1
ls = []
lsf = []
for i in range(n):
    f2 = f1 + f0
    lsf.append(f2)
    f0 = f1
    f1 = f2
    i += 1
for j in range(1,n+1):
    if j in lsf:
        ls.append("+")
    else:
        ls.append("-")

for i in ls:

    a = "".join(ls)

print(a)
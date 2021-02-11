n = input()

s = list(set(n))
flag = True

for i in s:

    a = n.count(i)
    if a % 2:
        flag = False

if flag:
    print("khoob")
else:
    print("bad")
    


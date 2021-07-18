a = input()
ooo = a
a = a.replace(' ', '')
first = a.index('+')
second = a.index('=')
b = a[:first]
c = a[first+1:second]
d = a[second+1:]

if '#' in b:
    res = str(int(d) - int(c))
    eq = b
elif '#' in c:
    res = str(int(d) - int(b))
    eq = c
else:
    res = str(int(b) + int(c))
    eq = d

if len(eq) > len(res) + 1:
    print(-1)
elif len(eq) == len(res) + 1:
    eq = eq.replace('#', '')
    if eq == res:
        print(eq)
    else:
        print(-1)
else:
    equal = True
    while eq[0] != '#':
        if eq[0] != res[0]:
            equal = False
            break
        eq = eq[1:]
        res = res[1:]
    while eq[-1] != '#':
        if eq[-1] != res[-1]:
            equal = False
            break
        eq = eq[:-1]
        res = res[:-1]
    if equal:
        print(ooo.replace('#', res))
    else:
        print(-1)
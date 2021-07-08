# x = list(map(int, input().split()))
l, r = list((input().split()))
l = int(l)
r = int(r)


def flip(c):
    c = list(c) 
    # print(c)
    for i in range(len(c)):
        if c[i] == '0':
            c[i] = '1'
        else:
            c[i] = '0'
    # print(c)
    return ''.join(c)

def concat():
    n = 100000
    s = '1'
    while len(s) < 100000:
        s = s + flip(s)

    # print(l, r)
    javab = s[l-1: r]
    return javab
    # for i in range(l-1, r):
    #     return s[i]

print(concat())
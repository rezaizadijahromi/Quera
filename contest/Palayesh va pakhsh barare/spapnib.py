# a, b, l = list(map(int, input().split()))
tedad_families = list(map(int, input().split()))
total = tedad_families[0]
wanted = list(map(int, input().split()))

def pakhsh(x, total):
    javab = []
    while total > 0:
        for i in x:
            if i == 1:
                total -= 1
                r = i - 1
                x.remove(i)
                # x.remove(i)
            else:
                print("We are in else")
                total -= 1
                r = i - 1
                x.remove(i)
                x.append(r) 

    return x

print(pakhsh(wanted, total))

# for i in x:
        #     print(i)
        #     if i == 0:
        #         x.remove(i)
        #     else:
        #         if i == 1:
        #             r = i - 1
        #             total -= 1
        #             # x.remove(i)
        #         else:
        #             total -= 1
        #             r = i - 1
        #             print(r)
        #             print(x)
        #             x.append(r)
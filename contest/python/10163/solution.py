from collections import Counter


def national_team():
    a,b,c = map(int, input().split())

    first = list(map(int, input().split()))
    second = list(map(int, input().split()))
    third = list(map(int, input().split()))
    nafar_aval = []
    nafar_dovom = []
    nafar_sevom = []
    koll = []

    yenafar = 0
    for i in range(first[0], first[1]):
        koll.append(i)
    donafar = 0
    for i in range(second[0], second[1]):
        koll.append(i)
    senafar = 0
    for i in range(third[0], third[1]):
        koll.append(i)

    # print(koll)
    col_koll = Counter(koll)
    col_koll = list(col_koll.values())
    # print(col_koll)
    yenafar = col_koll.count(1)
    donafar = col_koll.count(2)
    senafar = col_koll.count(3)
    # print(yenafar)
    # print(donafar)
    # print(senafar)


    calculate = (yenafar * 1 * a) + (donafar * 2 * b) + (senafar * 3 * c)

    return calculate

print(national_team())
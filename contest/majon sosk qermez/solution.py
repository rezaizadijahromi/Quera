a, b, c, d, m = list(map(int, input().split()))

first = a + (m * c)
second = b + (m * d)

if first > second:
    if c > d:
        print('Eyval baba!')

    else:
        print('Naaa, eshtebahe!')

else:
    if c < d:
        print("Eyval baba!")

    else:
        print('Naaa, eshtebahe!')



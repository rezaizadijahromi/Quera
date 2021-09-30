# def pardakht():
#     p, q = map(int, input().split())

#     jadval = [list(map(int, input().split())) for i in range(p)]

#     payment = []
#     for i in range(p):
#         start, finish = map(int, input().split())
#         payment.append(finish-1)

#     return payment, jadval

# def destination():
#     finished, position = pardakht()

#     hazine = 0
#     for i,j in zip(position, finished):
#         hazine += i[j]

#     return hazine

# print(destination())

def snapp():

    n, m = map(int,input().split())
    a = [list(map(int,input().split())) for i in range(n)]
    x = [0 for i in range(m)]
    y = [0 for i in range(m)]
    payment = 0
    for i in range(m):
        x[i], y[i] = map(int, input().split())
        payment += a[x[i]-1][y[i]-1]

    return payment

print(snapp())
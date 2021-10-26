

# def kevin():
#     n = int(input())
#     power = []

#     for i in range(n+1):
#         chap = i
#         rast = n - i
#         power.append(min(chap, rast))

#     calc = sum(power) / (n+1)

#     return calc

# print(kevin())
    # rast = n - i
    # chap = i
# import numpy as np

# n = int(input())
# power = []
# if n == 0 or n== 1:
#     calc = 0
# elif n == 2:
#     calc = 0.333333
# else:
#     for i in range(n+1 // 2):
#         power.append(i)
#     calc = sum(power * 2) / (n+1)

# calc = np.mean(power)


# n = int(input())
# # calc = [min(i, n-i) for i in range(n+1)]
# print('{0:.6f}'.format(sum([min(i, n-i) for i in range(n+1)]) / (n+1) ))
# # print('{0:.6f}'.format(sum(calc) / (n+1)))


n = int(input())
x = 0

if n % 2 != 0:
    for i in range(1, n//2 + 1):
        x += i
    answer = (n - 1) / 4
    print(answer)
else:
    for i in range(1, n//2 +1 ):
        x += i
    answer = (((x * 2) - (n / 2)) / (n+1))
    print(answer)
print(answer)
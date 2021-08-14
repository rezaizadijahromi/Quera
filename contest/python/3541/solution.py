import math
n = int(input())

if n % 2 == 0:
    print(round(n ** 2 / 48))

else:
    print(round((n+3) ** 2 / 48))

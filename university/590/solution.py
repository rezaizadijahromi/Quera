import math

def lcm(a, b):
    return abs(a*b) // math.gcd(a, b)

def gcd(x , y):
    if y == 0:
        return x
    else:
        return gcd(y, x % y)

x, y = list(map(int, input().split()))

g = gcd(x,y)
l = lcm(x,y)

print(g, l)


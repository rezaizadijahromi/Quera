def gcd(x , y):
    if y == 0:
        return x
    else:
        return gcd(y, x % y)


x = int(input())
y = int(input())


print(gcd(x,y))


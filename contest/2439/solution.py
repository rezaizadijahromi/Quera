import math
inputs = list(map(int, input().split()))
x = inputs[0]
search = str(inputs[1])
fact = str(math.factorial(x))

javab = fact.count(search)

print(javab)

# print(str(math.factorial(x)).rstrip('0')[-1])

n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

result = 0
for num1, num2 in zip(a, b):
    adad = num1 * num2
    result += adad
print((result))

n = int(input())

# def light_key(n):
#     stack = []
#     for i in range(0, n):
#         stack.append(input())
#     s = ''.join(stack)

#     n = s.count('01') + s.count('10')

#     return n

# print(light_key(n))


### First Try
def light_key1(n):
    stack = []
    count = 0
    j = 0
    for i in range(0, n):
        stack.append(int(input()))

    for j in range(0, len(stack)):
        # if j < n:
        print("stack :", stack[j])
        if stack[j] != stack[j+1]:
            count += 1
        else:
            break

    print(count)

light_key1(n)
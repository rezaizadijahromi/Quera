a,b, x = map(int, input().split())
stack_a = []
stack_b = []

def khab_popak(a, b, x):
    
    for i in range(1, a+1):
        # print(i)
        if a % i == 0:
            stack_a.append(i)
    for j in range(1, b+1):
        if b % j == 0:
            stack_b.append(j)

    # print(stack_a, stack_b)
    counter = 0
    for i in stack_a:
        for j in stack_b:
            if i + j <= x:
                counter += 1
    return counter


print(khab_popak(a, b, x))
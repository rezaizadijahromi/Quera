n = (int(input()))

list1 = list(str(n))
sume = 0
for i in list1:
    sume += int(i) 

def prime():


    counter = 0
    stack = []
    for num in range(n+1,100000):
        if num > 1:  
            for i in range(2,num):  
                if (num % i) == 0:  
                    break  
            else:  
                stack.append(str(num))
                if len(stack) == sume:
                    break

    # print(stack)
    return stack[-1]
        

print(prime())
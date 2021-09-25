t = int(input())
L = [ int(input()) for k in range(t) ]

def digits_sum(x):
    return sum([ int(i) for i in str(x)])

def prime_check(n):
    for i in range(2,int(n/2)+1):
        if n%i == 0:
            return False
    if n == 1:
        return False
    return True

def prime_divisors_sum(n):
    G = []
    for i in range(1,n+1):
        if n%i == 0:
            G.append(i)
    return sum([ j for j in G if prime_check(j) ])

for i in L:   
    c = 0
    for x in range(1,i-2):
        if i == prime_divisors_sum(x) +  digits_sum(x) + x:
            c = 1
            break
    if c == 1 :
        print("Yes")
    else:
        print("No")   
    

    
    
    
    
    
    
            


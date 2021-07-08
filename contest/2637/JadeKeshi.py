n = int(input())

if n % 2 == 0:
    even = n // 2
    even1 = even
    print((even+1)*(even1+1))
    

else:
    odd = n // 2 + 1
    
    odd1 = odd + 1

    print(odd * odd1)
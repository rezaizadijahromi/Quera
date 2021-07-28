def nextPowerOf2(n): 
    count = 0; 
    if (n and not(n & (n - 1))): 
        return n 
      
    while( n != 0): 
        n >>= 1
        count += 1
      
    return 1 << count; 
  
  
n = int(input())
print(nextPowerOf2(n)) 
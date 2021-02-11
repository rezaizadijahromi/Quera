import math
input1 = list(map(int,input().split()))

Number = input1[0]
Tedad = input1[1]

for i in range(Tedad):
    Number = Number / 2 
    
    

print(math.floor(Number))
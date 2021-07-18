n = int(input())

counter = 0
tedad = 0

i = 1
j = 1
for i in range(1,n + 1):
    
    for j in range(1,i + 1):
        
        if i % j == 0:
            counter += 1
            tedad += j

print(counter,tedad)
            

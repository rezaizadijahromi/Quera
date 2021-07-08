k = int(input())
ramz = input()

jay = []
javab = 0
for i in ramz:
    re = jay.append(i)
    


for i in range(k):
    x = input()
    x1 = x[::-1]
    z = x1.find(jay[i])
    z += 1
    y = x.find(jay[i])
    javab += min(y,z)
    i += 1



    
print(javab)
n,m = map(int,input().split())

boz = []
javab = {}
c = 0
answer = []

for i in range(n):
    boz.append(input().split())
    javab[boz[i][0]] = boz[i][1]

akhar = input().split()

for j in akhar:
    for k,v in javab.items():
    
        if k == j:
            answer.append(v+" kachal!")
            break
    else:
        answer.append("kachal!")
            

           

print(*answer)

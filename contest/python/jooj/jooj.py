n = int(input())

jade = list(map(int, input().split()))
count = jade[0]
jadeha = jade[1:]
counter = 0
javab= False

for i in jadeha:
    if i > count:
        counter += 1
    
    if counter >= 1:
        if count > i:
            javab = True
            break
    count = i

# print(count)
if javab:
    print('Ey baba :(')
else:
    print('Bah Bah! Ajab jooji!')

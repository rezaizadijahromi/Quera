lst = []
lst1 = []
lst2 = []

for p in range(4):
    input1 = list(map(str,input().split()))

    if input1[1] == 'U':
        lst.append(input1)

    elif input1[1] == 'R':
        lst1.append(input1)
    
    elif input1[1] == 'L':
        lst2.append(input1)


if len(lst1) > 1:
    if len(lst2) == 2:
        print(lst1[0][0])
    else:
        print(lst1[1][0])

elif len(lst2) > 1:

    if len(lst2) == 2:
        print(lst2[0][0])
    else:
        print(lst2[1][0])
    





a,b,c,d,e,f = list(map(int, input().split()))
list1 = []
list2 = []
for i in range(1):
    list1.append(a)
    list1.append(b)
    list1.append(b)
    list2.append(d)
    list2.append(e)
    list2.append(f)

list1 = sorted(list1)
list2 = sorted(list2)

m11 = list1[0] * list1[1] * list1[2]
m1 = list1[0] * list1[1]
m2 = list1[0] * list1[2]
m3 = list1[2] * list1[1]

m44 = list2[0] * list2[1] * list2[2]

m4 = list2[0] * list2[1]
m5 = list2[0] * list2[2]
m6 = list2[2] * list2[1]


if m1 >= m4 or  m11 >= m44:
    print('zende mimuni')
elif m2 >= m5 or m11 >= m44:
    print('zende mimuni')
elif m3 >= m6 or m11 >= m44:
    print('zende mimuni')

else:
    print('dari mimiri')




# if list2[0] <= list1[0] and list2[1] <= list1[1]:
#     print('zende mimuni')
# else:
#     print('dari mimiri')


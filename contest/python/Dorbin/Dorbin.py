# list1 = []
# list2 = []
# a1, b1 = list(map(int, input().split()))
# a2, b2 = list(map(int, input().split()))
# a3, b3 = list(map(int, input().split()))


# list1.append(a1)
# list1.append(a2)
# list1.append(a3)

# for i in list1:
#     javab1 = i
#     if javab1 != i:
#         javab1 = i


# list2.append(b1)
# list2.append(b2)
# list2.append(b3)


# for i in list2:
#     javab2 = i
#     if javab2 != i:
#         javab2 = i


# print(str(javab1) + " " + str(javab2))



list1 = []
list2 = []
a1, b1 = list(map(int, input().split()))
a2, b2 = list(map(int, input().split()))
a3, b3 = list(map(int, input().split()))


list1.append(a1)
list1.append(a2)
list1.append(a3)


list2.append(b1)
list2.append(b2)
list2.append(b3)


if list1[0] == list1[1]:
    javab1 = list1[2]

elif list1[0] == list1[2]:
    javab1 = list1[1]

elif list1[1] == list1[2]:
    javab1 = list1[0]

if list2[0] == list2[1]:
    javab2 = list2[2]

elif list2[0] == list2[2]:
    javab2 = list2[1]

elif list2[1] == list2[2]:
    javab2 = list2[0]



print(str(javab1) + " " + str(javab2))
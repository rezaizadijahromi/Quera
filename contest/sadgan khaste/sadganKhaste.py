first = int(input())
second = int(input())
f1 = first
f2 = second
revers1 = 0
revers2 = 0
while f1 and f2 > 0:
    reminder1 = f1 % 10
    revers1 = (revers1 * 10) + reminder1
    f1 = f1 // 10
    
    reminder2 = f2 % 10
    revers2 = (revers2 * 10) + reminder2
    f2 = f2 // 10


# print(revers1)
# print(revers2)

if revers1 > revers2:
    print(second,"<",first)
elif revers1 < revers2:
    print(first,"<",second)

# # elif second > first:
# #     print(first,"<",second)
# # elif second < first:
# #     print(first,"<",second)

elif first==second:
    print(first,"=",second)
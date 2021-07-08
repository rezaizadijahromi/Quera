input1 = list(map(int,input().split()))

ChannelList = []
first = input1[0]
second = input1[1]
third = input1[2]

for i in range(input1[0]):
    ChanelsName = input()
    ChannelList.append(ChanelsName)
j = 0
for j in range(third):
    
    if second < first:

        second += 1

    elif second == first:

        second = 1  

#     print(second)

# print(second)

print(ChannelList[second-1])



# for j in range(third):
#     if second < first:
#         second += 1
#     elif second == first:
#         second = 1
#     j += 1


# print(ChannelList[second])
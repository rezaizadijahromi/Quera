# n = int(input())
# reshte = list(input())
# s,t = map(int, input().split())
# min_ = min(s,t)
# max_ = max(s, t)
# shirink = reshte[min_ - 1: max_ ] 


# operation = 0
# counter = 0
# # for i in range(len(shirink)):
# #     if i != len(shirink):
# #         if shirink[i] == 'H':
# #             counter += 1
# #             if counter % 2 == 0:
# #                 operation += 1
# #                 counter = 0

# print(shirink)
# for i in range(len(shirink) - 1):
#     if i != len(shirink):
#         if shirink[i] == 'H':
#             counter += 1
#             if shirink[i + 1] != 'H' or (i+2) == len(shirink):
#                 operation += 1

# # javab = counter + operation

# print(operation)

# print(javab)

# print(shirink)
# print(counter)
# print(operation)


import math
n = int(input())
word = input()
s, t = map(int, input().split())

word = word[min(s,t) - 1: max(s, t)]

c = 0
for i in range(int(math.ceil(math.log2(len(word)))), -1, -1):
##    print(int(2 ** i) * 'H')
    c += word.count(2 ** i * 'H')
    word = word.replace(2 ** i * 'H', '')

print(c)
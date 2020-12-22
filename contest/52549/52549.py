# def good_cheff():
#     n = int(input())
#     top = []
#     while n != 0:
#         dict1 = dict()
#         list1 = []
#         for i in range(n):
#             ranks = list(map(int, input().split()))
#             ranks = ranks[1:]
#             for i in range(len(ranks)):
#                 if ranks[i] not in dict1:
#                     if i == 0:
#                         dict1[ranks[i]] = 3
#                     elif i == 1:
#                         dict1[ranks[i]] = 2
#                     elif i == 2:
#                         dict1[ranks[i]] = 1

#                 else:
#                     if i == 0:
#                         dict1[ranks[i]] += 3
#                     elif i == 1:
#                         dict1[ranks[i]] += 2
#                     elif i == 2:
#                         dict1[ranks[i]] += 1
        
#         max_value = max(dict1.values())
#         value_list = list(dict1.values())
#         key_list = list(dict1.keys())
#         pos = value_list.index(max_value)
#         print(key_list[pos])
    

#         # max_value = dict1[max(dict1.values())]
#         # top.append(dic1[max(dict1.values()])
        
# good_cheff()

def good_cheff():
    top = []
    while True:
        n = int(input())
        if n == 0:
            break
        scores = dict()
        list1 = []
        maxi = 0
        for i in range(n):
            ranks = list(map(int, input().split()))
            ranks = ranks[1:]
            for i in range(len(ranks)):
                if ranks[i] not in scores:
                    scores[ranks[i]] = 3 - i
                else:
                    scores[ranks[i]] += 3 - i

                if scores[ranks[i]] > maxi:
                    maxi = scores[ranks[i]]

        for i,j in scores.items():
            if j == maxi:
                list1.append(i)
        
        
        print(*sorted(list1))
        

        # print(maxi)
        # print(scores)

good_cheff()
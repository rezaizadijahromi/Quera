# from collections import Counter

# vorodi = input()

# cap = [
#     'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I',
#     'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R',
#     'S', 'T', 'U', 'U', 'V', 'W', 'X', 'Y', 'Z'
# ]

# low = [x.lower() for x in cap]


# def split_input(x):
#     input_x = [s for s in x]
#     lower_input = [s.lower() for s in x]
#     return (input_x, lower_input)

# def PES(x):
#     count = 0
#     check, lower_input = split_input(x)
#     next_word = []
#     counter = Counter(lower_input)
#     print(counter)
#     for i in check:
#         if i.isupper():
#             prev_index = cap.index(i)
#             upper_to_lower = i.lower()
#             count = counter.get(upper_to_lower)
#             # print(count)
#             if prev_index == 26:
#                 next_index = 0
#                 next_word += 'A'
#             else:
#                 next_index = (prev_index * count + 1) % 26 
#                 next_word += cap[next_index]
#         elif i.islower():
#             prev_index = low.index(i)
#             count = counter.get(i)
#             if prev_index == 26:
#                 next_index = 0
#                 next_word += 'a'
#             else:
#                 next_index = (prev_index * count + 1) % 26 
#                 next_word += low[next_index]

#     return next_word

# javab = PES(vorodi)
# javab = ''.join(javab)
# print(javab)



s = input()
res = ""
for i in s:
    p = s.count(i.lower()) + s.count(i.upper())
    if i >= 'a' and i <= 'z':
        res += chr(ord('a') + ((1 + (ord(i) - ord('a')) * p) % 26))
    else:
        res += chr(ord('A') + ((1 + (ord(i) - ord('A')) * p) % 26))        
print(res)
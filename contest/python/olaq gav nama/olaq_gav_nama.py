# limit, a, b = list(map(int, input().split()))

# num = 0
# count = 0
# i = True

# arr_counter = 0
# mama_counter = 0
# print(limit)
# print(a)
# while i:
#     if count != limit:
#         count += 1
#         arr_counter += 1
#         count += a
#         count += 1
#         mama_counter += 1
#         count += b
#     else:
#         i = False
#         break

# print(arr_counter, mama_counter)



limit, a, b = list(map(int, input().split()))

count = 0
arr = 0
mama = 0
for i in range(limit):
    if (count+1) <= limit:
        arr += 1
        count += 1
    if count <= limit:
        count += a
    if (count+1) <= limit:
        mama += 1
        count += 1
    if count <= limit:
        count += b

    # else:
    #     break

print(arr, mama)
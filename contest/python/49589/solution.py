# index, col = map(int, input().split())

# jadval = [list(input()) for i in range(index)]

# # print(jadval)
# satr = []
# soton = []
# count_str = 0
# count_soton = 0
# for i in range(index):
#     count_str = 0
#     for j in range(col):
#         if jadval[i][j] == '*':
#             count_str += 1
#     satr.append(count_str)
        
# for i in range(col):
#     count_soton = 0
#     for j in range(index):
#         if jadval[j][i] == '*':
#             count_soton += 1
#     soton.append(count_soton)
        
# satr = satr[3:]
# # print(satr)
# l_counter = 0
# for i in soton:
#     if i >= 4:
#         for j in range(len(satr)):
#             if satr[j] >= 2:
#                 l_counter += 1
#                 satr[j] = satr[j] - 1

# print(l_counter)

# def get_input():
#     index, col = map(int, input().split())
#     jadval = [list(input()) for i in range(index)]

#     return (index, col, jadval)


# def count_index_columns():
#     index, col, jadval = get_input()
#     satr = []
#     soton = []
#     count_str = 0
#     count_soton = 0
#     for i in range(index):
#         count_str = 0
#         for j in range(col):
#             if jadval[i][j] == '*':
#                 count_str += 1
#         satr.append(count_str)
            
#     for i in range(col):
#         count_soton = 0
#         for j in range(index):
#             if jadval[j][i] == '*':
#                 count_soton += 1
#         soton.append(count_soton)
#     satr = satr[3:]
    

#     return (satr, soton)

# def solver():

#     satr, soton = count_index_columns()
#     l_counter = 0
#     for i in soton:
#         if i >= 4:
#             for j in range(len(satr)):
#                 if satr[j] >= 2:
#                     l_counter += 1
#                     satr[j] = satr[j] - 1

#     return l_counter

# print(solver())

index, col = map(int, input().split())

jadval = [list(input()) for i in range(index)]




def traverseLshape(a, n, m): 
      
    # for each column or each L shape 
    for j in range(0, m): 
  
        # traversing vertically 
        for i in range(0, n - j): 
            if a[i][j] == '*':
                print(a[i][j], end = " ")
  
        # traverse horizontally 
        for k in range(j + 1, m): 
            if a[i][j] == '*':
                print(a[n - 1 - j][k], end = " ")

traverseLshape(jadval, index, col)


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



def get_input():
    index, col = map(int, input().split())
    jadval = [list(input()) for i in range(index)]

    return (index, col, jadval)


def count_index_columns():
    index, col, jadval = get_input()
    # print(jadval)
    col_step = 0

    # for i in range(index):
    #     count_str = 0
    #     for j in range(index):
    #         if jadval[j][i] == '*':
    #             count_str += 1
    #             if count_str >= 4:
    l_counter = 0
    star_counter = 0
    i_stack = []
    j_stack = []
    pos_stack = []
    for i in range(index):
        for j in range(col):
            if jadval[i][j] == '*':
                i_stack.append(i)
                j_stack.append(j)
                pos_stack.append((i,j))

    i_stack = list(set(i_stack)) 
    j_stack = list(set(j_stack))

    dflf
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


print(count_index_columns())

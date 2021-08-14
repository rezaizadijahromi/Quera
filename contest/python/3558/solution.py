# n, m = map(int, input().split())

# n_stack = []
# m_stack = []


# for i in range(n):
#     n_stack.extend(list(map(int, input().split())))

# for i in range(m):
#     m_stack.extend(list(map(int, input().split())))

# m_stack = sorted(m_stack)
# n_stack = sorted(n_stack)

# for i in range(len(n_stack)+1):
#     for j in m_stack:
#         if n_stack[i] < j and n_stack[i+1] > j:
#             print(j)

# # for i,j in zip(n_stack, m_stack):
# #     if j > i:



# print(n_stack)
# print(m_stack)

# # for i in range(n):


def heavy():

    n, m = map(int, input().split())
    l, r = zip(* [map(int, input().split()) for i in range(n + m)])

    # print(l)
    # print(r)

    n_stack = set()
    m_stack = set()
    for i in range(n):
        n_stack.update(range(l[i], r[i] + 1))
        # print(a)

    for i in range(n, n + m):
        m_stack.update(range(l[i], r[i] + 1))

    # print(n_stack)
    # print(m_stack)

    return len(n_stack.intersection(m_stack))
    # print(len(n_stack.intersection(m_stack)))

print(heavy())
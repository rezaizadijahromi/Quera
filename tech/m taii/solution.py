def calculator(n, m, li):
    shirink = []

    for i in range(0,n,m):
        shirink.append(sum(li[i:i+m]))

    calc = 0
    for i in range(len(shirink)):
        if i % 2 == 0:
            shirink[i] = 1 * shirink[i]
        else:
            shirink[i] = -1 * shirink[i]

    calc = sum(shirink)

    return calc












# print(calculator(8, 1, [1, 2, 3, 4, 5, 6, 7, 8]))
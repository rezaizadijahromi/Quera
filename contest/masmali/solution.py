from math import factorial

def fact():
    n = int(input())
    reshte = input()
    khali = (2*n) - len(reshte)

    i_count = n - reshte.count('I')
    o_count = n - reshte.count('O')
    javab = 1
    list1 = [i_count, o_count]
    all_posible = 2 * factorial(n) * factorial(n)
    test = factorial(khali)

    javab = all_posible // test
    # print(all_posible)
    # print(list1)
    # for i in list1:
    #     javab *= factorial(i) 
 

    # print(javab)

    # # javab = factorials[0] // factorials[1]

    return javab

print(fact())










   # factorials = []
    # for i in list1:
    #     if i < 0: 
    #         return 0
    #     elif i == 0 or i == 1: 
    #         return 1
    #     else: 
    #         fact = 1
    #         while(i > 1): 
    #             fact *= i 
    #             i -= 1
    #         factorials.append(fact)
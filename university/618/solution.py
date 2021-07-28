# def Diamond(rows): 
#     n = 0
#     for i in range(1, rows + 1): 
#         for j in range (1, (rows - i) + 1): 
#             print(end = " ") 
#         while n != (2 * i + 1): 
#             print("*", end = "") 
#             n = n + 1
#         n = 0
#         print() 
#     k = 1
#     n = 1
#     for i in range(1, rows): 
#         for j in range (1, k + 1): 
#             print(end = " ") 
#         k = k + 1

#         while n <= (2 * (rows - i) + 1): 
#             print("*", end = "") 
#             n = n + 1
#         n = 1
#         print() 
# rows = int(input())
# Diamond(rows) 


# h = int(input())

# for i in range(h):
#     print(" "*(h-i), "*"*(i*2+1))
# for i in range(h-2, -1, -1):
#     print(" "*(h-i), "*"*(i*2+1))
# n = int(input())

# for i in range(n):
#     print(' '*(n-i-1) + '*'*((2*i)+1) )
# for i in range(n):
#     print(' '*(i+1) + '*'*((2*((n-1)-i))-1))


side = int(input())

for x in list(range(side)) + list(reversed(range(side-1))):
    print('{: <{w1}}{:*<{w2}}'.format('', '', w1=side-x-1, w2=x*2+1))
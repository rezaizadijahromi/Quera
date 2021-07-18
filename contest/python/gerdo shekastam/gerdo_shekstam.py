n, x, y = list(map(int, input().split()))


count1 = 0
count2 = 0


i = 0
while i * x <= n: 
        
    if (n - (i * x)) % y == 0: 
        count1 = i
        count2 = int((n - (i * x)) / y)
    i = i + 1
n = 0

if count1 or count2:
    print(f"{count1} {count2}")
else:
    print(-1)


# if n%x == 0:
#     while n > 0:
#         n -= x
#         count1 += 1
# elif n % y == 0:
#     while n > 0:
#         n -= y
#         count2 += 1
# elif n % x != 0 and n % y != 0:
#     while n > 0:
#         if n > 0:
#             n -= x
#             count1 += 1
#         if n > 0:
#             n -= y
#             count2 += 1

# if n != 0:
#     print(-1)
# else:
#     print(f"{count1} {count2}")


# def solution (a, b, n): 
  
#     i = 0
#     while i * a <= n: 
          
#         if (n - (i * a)) % b == 0: 
#             print("x = ",i ,", y = ", 
#                int((n - (i * a)) / b)) 
#             return 0
#         i = i + 1
      
#     print("No solution") 

# if n%x == 0:
#     while n > 0:
#         n -= x
#         count1 += 1
# elif n % y == 0:
#     while n > 0:
#         n -= y
#         count2 += 1
# else:
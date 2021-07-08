import re
def find_fav():
    s = (input())
    n = int(input())
    strings = []
    count = 0
    i = 0 
    j = 0
    for i in range(n):
        t = input()
        status = re.findall(s, t)
        if len(status) != 0:
            count += 1
        # if status is not None:
        #     print(status)
        #     count += 1

    # print(count)
    # while n > 0:
    #     string = input()
    #     if len(string) > len(s):
    #         while i < len(string) and j < len(s):
    #                 if string[i] == s[j]:
    #                     j += 1
    #                 i += 1
    #     if j == len(s):
    #         count += 1

    #     n -= 1

    return count

print(find_fav())
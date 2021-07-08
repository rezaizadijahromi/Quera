def present():
    s = input()

    zero_count = s.count('0')

    if len(s) == zero_count:
        return 0
    else:
        s = s.lstrip('0')
        return s
    
    
    # i = 0
    # while i < len(s):
    #     if s[i] != '0':
    #         break
    #     i += 1

    # return i
     
print(present())
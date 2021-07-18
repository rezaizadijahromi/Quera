def great_tree():
    n = int(input())
    a = list(input())
    m = int(input())
    b = list(input())
    
    maxi = 0
    i = 0
    j = 0

    while i < len(a) and j < len(b):
        if a[i] == b[j]:
            i += 1
            j += 1
        else:
            break


    print(len(a) - i + len(b) - j)



great_tree()
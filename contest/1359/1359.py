def kepp_the_order(n):
    y = "YES"
    ne = "NO"
    ans = []
    for k in range((n)):
        string = input()
        sub_str = input()

        i = 0
        j = 0

        while i < len(string) and j < len(sub_str):
            if string[i] == sub_str[j]:
                j += 1
            i += 1

        if j == len(sub_str):
            ans.append(y)
            continue

        i = 0
        j = 0

        rev = string[::-1]
        # print(rev)

        while i < len(rev) and j < len(sub_str):
            if rev[i] == sub_str[j]:
                j += 1
            i += 1

        if j == len(sub_str):
            ans.append(y)

        else:
            ans.append(ne)

    # print('_____________________')
    for i in ans:
        print(i)

n = int(input())

kepp_the_order(n)



        


        
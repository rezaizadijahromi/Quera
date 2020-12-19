def bank_varification():
    flag = True
    # odd = []
    # even = []
    # javab = []
    while flag:
        qa = list(map(int, input().replace(" ", '')))
        odd = []
        even = []
        javab = []
        if sum(qa) > 0:
            for i in range(len(qa)):
                if i % 2 == 0:
                    odd.append(qa[i] * 2)
                else:
                    even.append(qa[i])

        # print(even)

            minus_9 = []
            for i in range(8):
                # print(odd[i])
                if odd[i] > 9:
                    minus_9.append(odd[i] - 9)
                else:
                    minus_9.append(odd[i])

            # print(odd)
            # print(even)
            # print(minus_9)

            even = sum(even) 
            odd = sum(minus_9)

            result = even + odd

            if result % 10 == 0:
                print('Yes')
            else:
                print('No')
        else:
            flag = False
            break

        


(bank_varification())
def Tax():
    after_tax = []
    while True:
        income = int(input())
        if income == 0:
            break

        if income <= 1000000:
            after_tax.append(income)
            print(income)

        elif income > 1000000 and income <= 5000000:
            after_tax.append(int(income * .9))
            print(int(income * .9))

        else:
            after_tax.append(int(income * .8))
            print(int(income * .8))


    for i in after_tax:
        print(i)


Tax()
# print(Tax())
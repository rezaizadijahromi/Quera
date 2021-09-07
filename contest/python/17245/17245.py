def tax_man():
    a = input()
    b = input()
    c = input()

    # print('testing')
    # print(a)
    # print(b)
    # print(c)
    # print('testing')

    result = ""
    for i in range(0, len(a), 5):
        if a[i: i + 5] == "*****":
            result += "T"
        elif a[i: i + 5] == "oo*oo":
            result += "A"
        elif a[i: i + 5] == "**o**":
            result += "M"
        elif a[i: i + 5] == "*ooo*":
            if b[i: i + 5] == "oo*oo":
                result += "X"
            elif b[i: i + 5] == "*o*o*":
                result += "N"
    return result

print(tax_man())
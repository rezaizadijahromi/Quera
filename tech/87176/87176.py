def game(number):
    number = str(number)
    a, b = number[0], number[1]
    if int(a) >= int(b):
        return int(a) - int(b)
    else:
        return int(b) - int(a)

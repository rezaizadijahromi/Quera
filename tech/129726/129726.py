def separator(ls):
    odd = []
    even = []
    for item in ls:
        if item % 2 != 0:
            even.append(item)
        else:
            odd.append(item)
    return (odd, even)

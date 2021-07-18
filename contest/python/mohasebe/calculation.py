def calculation():
    max_each_row = []
    for i in range(4):
        vorodi = list(map(int, input().split()))
        find_max = max(vorodi)
        max_each_row.append(find_max)

    
    javab = max_each_row.index(max(max_each_row))

    return javab + 1

print(calculation())

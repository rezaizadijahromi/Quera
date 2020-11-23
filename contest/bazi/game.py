n = int(input())
list1 = list(map(int, input().split()))

def find_max_min(x):
    new_list = []

    list2 = sorted(list1)
    for i in range(len(list2)):
        if len(list2) != 0:
            new_list.append(list2[~i])
            new_list.append(list2[i])

    return (new_list[:n])

game = find_max_min(list1)
print(*game)


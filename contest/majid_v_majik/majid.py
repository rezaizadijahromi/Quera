from collections import Counter

def majid():
    n = int(input())
    majik_ha = list(map(int, input().split()))
    counter = Counter(majik_ha)
    store = []
    get_values = []
    min_values = counter.values()
    for i in min_values:
        get_values.append(i)

    min_values = min(get_values)
    # print(get_values)
    # for (key,values), get in zip(counter.items(), get_values):
    for key, values in counter.items():
        if values == min_values:
            store.append(key)


    print(min(store))
    # print(counter)
    # print(keys)
    # print(values)
    # min_values = min(values)
    # print(min_values)

    # print(counter[min_values])


majid()
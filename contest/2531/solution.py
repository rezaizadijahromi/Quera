def crime():
    x, y = list(map(int, input().split()))
    n = int(input())
    counter = 0

    for i in range(n):
        l, u = list(map(float, input().split()))

        # if l > x or l < y:
        #     counter += 1
        # if l < x and u > x :
        #     counter += 1
        # if u > x:
        #     counter += 1
        if l > x or u > x or u > y:
            counter += 1

    if counter > 1:
        mini = 1
        maxi = counter
    else:
        mini = 0
        maxi = 1


    print(mini, maxi)
crime()


def perfect(n):
    counter = 0
    for i in range(1, n):
        if n % i == 0:
            counter += i

    if counter == n:
        print("YES")

    else:
        print("NO")



n = int(input())

perfect(n)
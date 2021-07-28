def maqlob():
    n = input()

    reverse = int(n[::-1])
    n = int(n)

    if n == reverse:
        print("YES")
    else:
        print("NO")

maqlob()

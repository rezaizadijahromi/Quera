
def solution():
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    result = 0

    for i in range(5):
        for j in range(5):
            s = (((a[(i + 1) % 5] + b[(j + 1) % 5]) % 10) * 100) + (((a[(i + 2) % 5] +
                                                                      b[(j + 2) % 5]) % 10) * 10) + ((a[(i + 3) % 5] + b[(j + 3) % 5]) % 10)
            if s % 6 == 0:
                print("Boro joloo :)")
                return
    print("Gir oftadi :(")


solution()

def students(n):
    std = list(input().split())
    if len(std) == 1:
        print(f'{std[0]}: khodafez bacheha!')
    else:
        for i in range(len(std)):
            if i > 0:
                for j in range(i-1, -1, -1):
                    print(f'{std[i]}: salam {std[j]}!')

        for i in range(len(std)):
            print(f'{std[i]}: khodafez bacheha!')
            for j in range(i+1, len(std)):
                print(f'{std[j]}: khodafez {std[i]}!')


n = int(input())

students(n)
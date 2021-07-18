x, y = list(map(int, input().split()))
r = int(input())
dx, dy = list(map(int, input().split()))


if x <= dx and dx <= x+r:
    if dy >= y-r and dy <= y:
        print("Mahdi")
    else:
        print('Parsa')
else:
    print('Parsa')

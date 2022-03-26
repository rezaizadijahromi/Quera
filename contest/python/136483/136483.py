n = int(input())
areas = []
for i in range(n):
    area = list(map(int, input().split()))
    areas.append(area)

start = int(input())
end = int(input())

new_init = []
for i in range(start, end + 1):
    new_init.append(i)

new_areas = []
for i in areas:
    for j in range(i[0], i[1] + 1):
        new_areas.append(j)

flag = True
for i in new_init:
    if i not in sorted(new_areas):
        flag = False

if flag:
    print("true")
else:
    print("false")

n = int(input())
areas = []
for i in range(n):
    start, finish = list(map(int, input().split()))
    areas.append(start)
    areas.append(finish)

start = int(input())
end = int(input())

new_init = []
for i in range(start, end + 1):
    new_init.append(i)

flag = True
for i in new_init:
    if start >= sorted(areas)[0] and end <= sorted(areas)[-1]:
        flag = True
    if i not in sorted(areas):
        flag = False

if flag:
    print("true")
else:
    print("false")

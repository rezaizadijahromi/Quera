numof, to_univ = [int(i) for i in input().split()]
redlamps = list()
# LENGTH , RED , GREEN
for i in range(numof):
    redlamps.append([int(i) for i in input().split()])

start = 0
where = 0
while where < to_univ:
    iso = False
    for i in redlamps:
        iso = False
        print(i[0])
        if i[0] == where:
            if i[1] > start % (i[1] + i[2]):
                start += i[1] - start % (i[1] + i[2])
        else:
            iso = True
    if iso:
        start += 1

    where += 1
print(start + 1)
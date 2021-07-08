n = int(input())

counter = 0
i = 1

for i in range(n + 1):

    for j in range(i):

        counter += 1

print(counter)
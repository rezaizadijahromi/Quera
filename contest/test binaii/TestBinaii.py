n = int(input())

fact = input()
person = input()

counter = 0
for i,j in zip(fact,person):
    if i == j:
        counter += 1
    else:
        continue

print(len(fact) - counter)

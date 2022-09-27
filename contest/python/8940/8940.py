n, p, q = list(map(int, input().split()))

names = set()
for i in range(n):
    name = input("")
    name = name[0:p] + name[len(name)-q:len(name)]
    names.add(name)

print(len(names))
stack = []
for i in range(0,5):
    data = input()
    stack.append(data)

javab = []
for count, j in enumerate(stack):
    if "HAFEZ" in j or 'MOLANA' in j:
        javab.append(count+1)

if len(javab) == 0:
    print('NOT FOUND!')
else:
    print(*javab)
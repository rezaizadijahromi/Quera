def konab(n):
    users_ip = {}
    users_name = {}
    users = {}
    index = 0
    errors = ['_', '*', '$', '#']
    for _ in range(n):
        line = input().split()
        line[1] = line[1].split(':')
        if line[0] == '1':
            for i in errors:
                if i in line[1][1]:
            else:
                users_ip[line[1][0]] = index
                users_name[line[1][1]] = index
                users[index] = 0
                index += 1
    
        elif line[0] == '2':
            users[users_ip[line[1][0]]] -= int(line[1][2])
            users[users_name[line[1][1]]] += int(line[1][2])
        elif line[0] == '3':
            print(users[users_ip[line[1][0]]])

    print('_____________________________________')
    print(users)
    print(users_name)
    print(users_ip)
    print('_____________________________________')


n = int(input())
(konab(n))



# if '_' in line[1][1] or '*' in line[1][1] or '#' in line[1][1] or '$' in line[1][1]:
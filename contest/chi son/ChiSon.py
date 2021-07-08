import json

env = {}

n = int(input())

for _ in range(n):
    line = input()

    if len(line) >= 5 and line[0:5] == 'print':
        line = line[6:]
        ind = line[line.index('[')+1:line.index(']')]

        if ind[0] != '"':
            ind = int(ind)
        else:
            ind = ind[1:len(ind)-1]

        print(env[ line[:line.index('[')] ][ ind ])
    else:
        st = line.index('[') if '[' in line else line.index('{')
        env[ line.split(' ')[0] ] = json.loads( line[st:] )

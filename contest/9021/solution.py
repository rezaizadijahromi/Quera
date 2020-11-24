def off_lamps():
    n = int(input())
    komak = {}
    lams = list(map(int, input().split()))
    switches = list(map(int, input().split()))
    for i,j in zip(lams, switches):
        komak[i] = j

    on_lamps = []
    for i,j in komak.items():
        if j == 1:
            on_lamps.append(i)
    on_lamps = sorted(on_lamps)
    
    print(*on_lamps)

off_lamps()



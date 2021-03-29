def RatHole():
    javab = []
    mouse, hole = list(map(int, input().split()))
    if mouse == hole:
        print("Saal Noo Mobarak!")
    elif hole > mouse:
        for i in range(mouse, hole):
            javab.append("R")
    elif mouse > hole:
        for i in range(hole, mouse):
            javab.append("L")

    return "".join(javab)

rathole = print(RatHole())
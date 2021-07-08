LebasSize = list(map(int,input().split()))
HadieSize = list(map(int,input().split()))

for i,j in (LebasSize,HadieSize):
    if LebasSize[0] >= HadieSize[0] and LebasSize[1] >= HadieSize[1]:
        y = "yes"
    else:
        y = "no"
    

print(y)
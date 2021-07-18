num1 = int(input())

def findnext(ii):
    iis=list(map(int,str(ii)))
    for i in reversed(range(len(iis))):
        if i == 0:
            return 0
        if iis[i] > iis[i-1] :
            break        
    left,right=iis[:i],iis[i:]
    for k in reversed(range(len(right))):
        if right[k]>left[-1]:
           right[k],left[-1]=left[-1],right[k]
           break

    javab = int("".join(map(str,(left+sorted(right)))))

    if javab == ii:
        javab = 0
        
    else:
        return javab 


print(findnext(num1))
            
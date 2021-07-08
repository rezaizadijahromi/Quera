adad = list(map(int,input()))
jame = 0
j = 0
a = 0
p = 0
b = 0
for i in adad:

    jame += i
    

if jame > 9:
    while jame > 0:       
        a = jame % 10
        j += a
        jame = jame // 10   

     
    if j > 9:
        while j > 0:
            b = j % 10
            p += b
            j = j // 10 
        print(p)   

    else:
        print(j)
     

else:
    print(jame)   

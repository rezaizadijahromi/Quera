r,c = map(int,input().split())

a = 11 - r
if c <= 10 :
    d = "Right"
    s = c

else:
    d = "Left"
    s = 21 - c

print(d,a,s)


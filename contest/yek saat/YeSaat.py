import math

input1 = list(map(int,input().split()))

h = input1[0]
m = input1[1]

h = 12 - h
m = 60 - m


if h < 10:

    if m == 60 and h == 12:
        h = 0
        m = 0
        

    if m < 10 :
        print("0{h}:0{m}".format(h = h,m = m))

    
    elif m == 60:
        m = 59
        print("0{h}:{m}".format(h = h,m = m))

    elif m == 0:
        m = 0
        print("0{h}:0{m}".format(h = h,m = m))


        

    elif m >= 10:
        print("0{h}:{m}".format(h = h,m = m))
        
elif h >= 10:

    if m == 60 and h==12:
        print("00:00")

    elif m == 0:
        m = 0
        print("{h}:0{m}".format(h = h,m = m))

    elif h == 12:
        h = 11
        print("{h}:{m}".format(h = h,m = m))


    
    elif m == 60:
        m = 59
        print("{h}:{m}".format(h = h,m = m))

    
    elif m < 10:
        print("{h}:0{m}".format(h = h,m = m))

    elif m >= 10:
        print("{h}:{m}".format(h = h,m = m))

# if h < 6:
#     h += 2 * abs(h - 6)

# else:
#     h = abs(h - 12)

# if m < 30:
#     m += 2 * abs(m - 30)

# else:
#     m = abs(m - 60)
# Result = "%02d:%02d"
# print(Result % (h%12,m%60))
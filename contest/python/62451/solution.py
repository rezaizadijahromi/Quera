def torab():

    vorodi = []
    for i in range(4):
        vorodi.append(int(input()))

    x1 = vorodi[0]
    v1 = vorodi[1]
    x2 = vorodi[2]
    v2 = vorodi[3]


    if v1 - v2 == 0:
        
        print('WAIT WAIT')

    else:

        v_teta = v1 - v2
        x_teta = x1 - x2

        a = v_teta // x_teta

        if a < 0:
            print('SEE YOU')

        else:
            print('BORO BORO')


torab()
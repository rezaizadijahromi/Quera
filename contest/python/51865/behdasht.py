nomre = int(input())
roozaye_safar = int(input())


if roozaye_safar == 0:
    nomre = 20

elif roozaye_safar == 7:
    nomre = nomre

elif nomre <= roozaye_safar:
    nomre = 0
else:
    for i in range(0, roozaye_safar):
        nomre -= 1



print(nomre)            

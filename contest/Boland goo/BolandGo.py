kalame = input()

print(kalame)
for i in range(1,len(kalame)):

    temp1 = kalame[i:i+1]
    temp2 = kalame[i:]
    temp3 = temp1

    for j in range(1, i):
        temp1 += temp3

    print(temp1 + temp2)
  #  print(temp2)
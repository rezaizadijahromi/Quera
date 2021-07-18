input1 = list(map(int,input().split()))

row = input1[0]
column = input1[1]
lst = []
counter = 0
input2 = ""

for i in range(row):
    input2 += input()

print(input2.count('*'))
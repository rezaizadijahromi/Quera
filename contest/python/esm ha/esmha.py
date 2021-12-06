n = int(input())
ans1 = 0
for i in range(n):
	name = input()
	dif = ""
	for j in name:
		if j not in dif:
			dif = dif + j
	ans1 = max(ans1, len(dif))
print(ans1)
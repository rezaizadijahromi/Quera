cnt = int(input())
names = {}
for i in range(cnt):
	name , family = input().split(" ")
	if name in names.keys(): 
		 names[name] += 1
	else :
		names[name] = 1
ans = sorted(names.values())[-1]
print(ans)
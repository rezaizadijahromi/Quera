n = int(input())
days = []
for i in range(n):
    days.append(int(input()))


def find_kmm(x):
    for i in x:
        for j in range(30):
            m = j + 1


def returns_new_thelist(ll):
	if 3 in ll:
		ll.remove(3)
	for i in ll:
		if checks_if_prime(i) == True:
			ll.remove(i)
	return ll    

def checks_if_prime(n):
	if n == 2:
		return True
	import math
	for i in range(math.ceil(0.5*n), 1, -1):
		if n % i == 0:
			return False
		elif i == 2:
			return True

def final_lcm(thelist):
	factors = 1
	previous_thelist = thelist
	prime_thelist = list(set(thelist) - set(returns_new_thelist(previous_thelist)))
	factors = 1
	for i in prime_thelist:
		factors = factors*i
	new_thelist = returns_new_thelist(previous_thelist)
	for i in range(1, 10000000000):
		s_empty = []
		for j in new_thelist:
			if i % j  == 0:
				s_empty.append(True)
		if len(new_thelist) == len(s_empty):
			initial_lcm = i
			break
	final_lcm = factors * initial_lcm
	return final_lcm

def final_answer(x):
	javab = final_lcm(x)
	javab = javab % 30
	javab += 1

	return javab

print(final_answer(days))















from math import gcd
lcm = days[0]
for i in days[1:]:
  lcm = lcm*i//gcd(lcm, i)

javab = lcm % 30 
javab += 1
print(javab)
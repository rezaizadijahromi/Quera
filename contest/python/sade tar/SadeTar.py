first = int(input())
second = int(input())
third = int(input())
fourth = int(input())

sum = first + second + third + fourth
ave = sum/4
product = first * second * third * fourth
mx = max(first,second,third,fourth)
mi = min(first,second,third,fourth)

print("Sum :","{:.6f}".format(sum))
print("Average :","{:.6f}".format(ave))
print("Product :","{:.6f}".format(product))
print("MAX :","{:.6f}".format(mx))
print("MIN :","{:.6f}".format(mi))
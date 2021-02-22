n = int(input())
arr = []
for i in range(n):
    arr.append(int(input()))
    x = arr[i]
    for j in range(1, len(arr)):
        if arr[j] == 0:
            k = 0
            kk = j
            while k < x:
                if arr[kk] == 0:
                    k += 1
                kk += 1
            if k == x:
                while arr[kk] != 0:
                    kk += 1
                arr[kk] = i
                break

for i in range(1 ,len(arr) - 1):
    print(arr[i])

print(arr[len(arr)-1])


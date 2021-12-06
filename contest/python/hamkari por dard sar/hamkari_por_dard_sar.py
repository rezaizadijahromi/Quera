n, m = map(int,input().split())
moh_jav = set(map(int,input().split()))
mostafa = set(map(int,input().split()))

if moh_jav == mostafa:
    print('Both')
elif mostafa.issubset(moh_jav):
    print('Mostafa')
elif moh_jav.issubset(mostafa) :
    print('Mohammad Javad')
else:
    print('None')

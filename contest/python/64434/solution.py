n, m = list(map(int, input().split()))

n_fix = n * 3
m_fix = m * 3

for i in range(n_fix):
    for j in range(m_fix):
        k = ((i / n) + 1) * ((j / m) + 1)
        if k == 1 or k == 3 or k == 4 or k == 9:
            print('X')
        else:
            print('.')




n = int(input())
test_key = list(input())

keyvoon = []
nezam = []
shir_farhad = []

for i in range(n // 6 + 1):
    keyvoon.extend(['3','3','1','1','2','2'])

for i in range(n // 3 + 1):
    nezam.extend(['1','2','3'])

for i in range(n // 4 + 1):
    shir_farhad.extend(['2','1','2','3'])

keyvoon = keyvoon[:len(test_key)]
nezam = nezam[:len(test_key)]
shir_farhad = shir_farhad[:len(test_key)]

keyvoon_counter = 0
for i,j in zip(test_key, keyvoon):
    if i == j:
        keyvoon_counter += 1

nezam_counter = 0
for i,j in zip(test_key, nezam):
    if i == j:
        nezam_counter += 1

        
shir_farhad_counter = 0
for i,j in zip(test_key, shir_farhad):
    if i == j:
        shir_farhad_counter += 1

grades = {
    'keyvoon':keyvoon_counter,
    'nezam':nezam_counter,
    'shir farhad': shir_farhad_counter
}
sorted_grades = sorted(grades)

max_grade = max(keyvoon_counter, nezam_counter, shir_farhad_counter) 
print(max_grade)

best_lists = []
for i,j in grades.items():
    if j == max_grade:
        print(i)
        # best_lists.append(i)



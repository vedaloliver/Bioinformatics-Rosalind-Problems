s = open('rosalind_dna.txt')

fils = s.read()
lists = []

for i in fils:
    lists += i

A_count = 0
C_count = 0
G_count = 0
T_count = 0

for i in lists:
    if i == 'A':
        A_count += 1
    elif i == 'G':
        G_count += 1
    elif i == 'C':
        C_count += 1
    elif i == 'T':
        T_count += 1

print (A_count,C_count,G_count,T_count)
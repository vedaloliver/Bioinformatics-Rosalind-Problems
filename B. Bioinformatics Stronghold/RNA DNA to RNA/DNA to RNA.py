s = open('rosalind_rna.txt')

fils = s.read().strip('\n')
lists = []

for i in fils:
    lists += i

for n,i in enumerate(lists):
    if i == 'T':
        lists[n]= 'U'
    
result = ''
for element in lists:
    result += str(element)

print (result)



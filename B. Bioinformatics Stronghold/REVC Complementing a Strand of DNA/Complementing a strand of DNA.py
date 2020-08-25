s = open('rosalind_revc.txt')

fils = s.read().strip('\n')
lists = []

for i in fils:
    lists += i

for n,i in enumerate(lists):
    if i == 'T':
        lists[n]= 'A'
    if i == 'A':
        lists[n]= 'T'
    if i == 'C':
        lists[n]= 'G'
    if i == 'G':
        lists[n]= 'C'
    
result = '' 
for element in lists:
    result += str(element)

resultrev = result[::-1]

print (resultrev)

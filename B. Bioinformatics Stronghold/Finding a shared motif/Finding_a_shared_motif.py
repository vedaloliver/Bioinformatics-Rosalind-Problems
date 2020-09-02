import itertools

## so this doesnt work

## while it does work for the very small amounts, it runs into a problem of it never stoppingcalculating 
##because the lengths of the sequences are so big 

## maybe it would be simpler to provide a boolean if it is in the other string
## if it is, show it is in where and only show the biggest
## but how do you do this

files = open('rosalind_lcsm.txt')

dataset = files.read()
print(dataset)

a =  '''GATTACA'''
b = 'TAGACCA'
c = 'ATACA'

a_list = []
for i in range(len(a)+ 1):
    for j in range(len(a)+ 1):
        if (bool(a[i:j])) == True and len((a[i:j])) >1 :
            a_list.append((a[i:j]))

print(len(a_list))

b_match = []
c_match = []
for j in a_list:
    if j in b:
        b_match.append(j)      
    if j in c:
        c_match.append(j) 

for i in b_match:
    if i in c_match:
        print (i)
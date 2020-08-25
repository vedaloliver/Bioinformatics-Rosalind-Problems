s = open('rosalind_2.txt', 'r')
strs = ''
for i in s:
    strs += i.strip('\n')

#print (strs)

#s = 'We tried list and we tried dicts also we tried Zen'

dicts = {}

for i in strs.split(' '):
    if i not in dicts.keys():
        dicts[i]= 0
    dicts[i] += 1

for key,value in dicts.items():
    print (key, value)



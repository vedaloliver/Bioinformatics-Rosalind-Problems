import itertools

# the number given
filez = open('rosalind_perm.txt')
x = int(filez.read())
# have to add +1 if not the index ends on the number before
x1 = x+1
#produces a range of numbers of the given n
y = list(range(1,x1))
#give a list of tuples of the permutations 
y1 = (list(itertools.permutations(y)))

# changes the tuples to strings which is retarded
# adds a total of permutations
total = 0
string = ''
for i in (y1):
    string += (str(i).replace(',', '').replace('(', '').replace(')', '')+ '\n')
    total += 1

print (total)
print (string)

#surprising that when given an n for 6, 720 permutations were given
# might be useful to write it to a docuemnt
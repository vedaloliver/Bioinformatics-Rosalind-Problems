files = open('rosalind_hamm.txt', 'r')

# pulls out the lines in the file and adds them to a list with each index as  a line
# rstrip takes away the newline element
listz = [] 
for i in files:
    listz.append(i.rstrip("\n"))

# goes through each element of the indexes in the list and adds them to their new list 
# each index will be a nucleotide
sl = []
tl = []
for i in listz[0]:
    sl += i
for i in listz[1]:
    tl += i

#checks if each element in the corresponding indexes are equal, if not it will add int to num 
num = 0
for i in range(len((sl))):
    if sl[i] != tl[i]:
        num += 1


#result
print (num)

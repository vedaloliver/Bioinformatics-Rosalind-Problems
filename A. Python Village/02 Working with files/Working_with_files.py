# while it introducted opening of files you knew this concept, but it showed the aspect of writing to new files

f = open('rosalind_ini5.txt','r')
# a file does not ned to be created, this does this for you yourself
m = open('output.txt', 'w')

# pulls the lines from the document and adds them to a list
words = []
for line in f:
    words.append(line.strip())

# the question asked you to  pull out the even lines of the docuement
odd = []
even = []
# spilts the list into odd and even into it's own list - odd was not needed but its here anyway
for i in range(0, len(words)):
    if i % 2:
        even.append(words[i])
    else:
        odd.append(words[i])

# writes the even parts of the list to a new file as the output
for i in even:
        m.write(str(i) + '\n')



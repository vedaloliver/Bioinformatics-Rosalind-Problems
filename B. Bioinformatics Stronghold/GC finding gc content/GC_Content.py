from Bio import SeqIO
##A nice task which wasnt too difficult in complexity

##  this was useful as it showed me how to get sequences from fasta files quite easily
files = SeqIO.parse('rosalind_gc.txt', 'fasta')
content = []
#looped over each sequence in the file
for i in files:
    G_count= 0
    C_count = 0
    #nested loop allowed to loop within each sequence itself
    for j in i.seq:
        # add both to a counter to find individual counts
        if j == 'C':
            C_count +=1
        elif j == 'G':
            G_count +=1 

    
    # adds the content to a list
    content.append([(((C_count+ G_count)/ len(i)*100)),i.id])

# the output. i was very stupid
print(max(content))
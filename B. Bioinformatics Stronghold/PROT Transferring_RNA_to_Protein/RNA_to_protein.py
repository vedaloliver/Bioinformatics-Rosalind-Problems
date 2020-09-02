
import re
#since the file here was so big, utilised reading the file and adding it as a string, which was simple
files = open('rosalind_prot.txt', 'r')
# just stole a dictionary from the internet as i wouldnt learn much from doing it myself
maps = {"UUU":"F", "UUC":"F", "UUA":"L", "UUG":"L",
       "UCU":"S", "UCC":"S", "UCA":"S", "UCG":"S",
       "UAU":"Y", "UAC":"Y", "UAA":"STOP", "UAG":"STOP",
       "UGU":"C", "UGC":"C", "UGA":"STOP", "UGG":"W",
       "CUU":"L", "CUC":"L", "CUA":"L", "CUG":"L",
       "CCU":"P", "CCC":"P", "CCA":"P", "CCG":"P",
       "CAU":"H", "CAC":"H", "CAA":"Q", "CAG":"Q",
       "CGU":"R", "CGC":"R", "CGA":"R", "CGG":"R",
       "AUU":"I", "AUC":"I", "AUA":"I", "AUG":"M",
       "ACU":"T", "ACC":"T", "ACA":"T", "ACG":"T",
       "AAU":"N", "AAC":"N", "AAA":"K", "AAG":"K",
       "AGU":"S", "AGC":"S", "AGA":"R", "AGG":"R",
       "GUU":"V", "GUC":"V", "GUA":"V", "GUG":"V",
       "GCU":"A", "GCC":"A", "GCA":"A", "GCG":"A",
       "GAU":"D", "GAC":"D", "GAA":"E", "GAG":"E",
       "GGU":"G", "GGC":"G", "GGA":"G", "GGG":"G",}

# file to string
dataset = files.read()
data_codon = []

#this loop functions as a way to split a string based on n, which in this case was three as a codon is three
#adds it to a list
for i in range(0,len(dataset), 3):
    data_codon.append(dataset[i:i+3])

protein_string = ''
# loops through the list, checks if dictionary key is present in each codon
# if it is it produces the necessary key
for i in data_codon:
    if i in maps.keys():
        protein_string+=(maps[i])

# was not outlined but stop codon was present at the end, simple list sliciing got rid of it
protein_string_stop_remove = protein_string[:-4]
print (protein_string_stop_remove)    



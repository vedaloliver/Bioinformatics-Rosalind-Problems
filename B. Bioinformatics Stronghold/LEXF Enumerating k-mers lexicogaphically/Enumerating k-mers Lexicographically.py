import itertools
from itertools import permutations

letters= 'ABCD'
n = 4

def perm(n, seq):
    for i in itertools.product(seq, repeat=n):
        print (str(i).replace(',', '').replace('(', '').replace(')', '').replace('\'', '').replace(' ', ''))

print (perm(n, letters))
a = 4881
b = 9486

sumz = 0
for i in range(b):
    if (i>=a) and ((i % 2) == 1):
        sumz += i

print (sumz)
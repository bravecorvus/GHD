# print square roots in Python language.  R. Brown, 9/2010 

import sys
from math import sqrt
if len(sys.argv) < 2:
    print("Enter in a set of space separated numbers so the program can set largest one to n, and caculate the all the square roots of 1 - n\n")
else:
    maxval = int(sys.argv[1])
    for count, data in enumerate(sys.argv):
        if count < 2:
            continue
        current = int(data)
        maxval = max(maxval, int(data))

    print("sqrt(n)\n--------")

    for n in range(1, maxval+1):
        print(sqrt(n))

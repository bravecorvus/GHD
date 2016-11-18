# Example of command-line arguments in Python3
# Prints any command-line arguments, one per line
# Usage:  python3 cmdargs.py arg1 arg2 ... 

import sys
# print(sys.argv)
maxval = int(sys.argv[1])
for count, data in enumerate(sys.argv):
    if count < 2:
        continue
    current = int(data)
    maxval = max(maxval, int(data))
print(maxval)
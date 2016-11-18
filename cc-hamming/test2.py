userinput = int("a23d", 16)
# print(userinput)
bindata = list(bin(userinput)[2:])
print(bindata)

# hamstring = ''.join([str(i) for i in bindata])
# finalint = int(hamstring, 2)
# print(hex(finalint))
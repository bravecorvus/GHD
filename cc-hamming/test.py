p1 = 0x3a
p2 = 0x66
mask = 0x0e
tmp = p1<<2
print(tmp)
tmp = p1 >> 1
print(tmp)
tmp = p1 & p2
print(tmp)
tmp = p1 & mask
print(tmp)
tmp = p1 | p2
print(tmp)
tmp = p1 ^ p2
print(tmp)
tmp  = (p1 >> 3) & 1
print(tmp)
tmp = (p2 >> 3) & 1
print(tmp)
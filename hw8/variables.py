def addn(x):
    global n
    return x + n

n = 7

val = int(input("Enter an integre value: "))
print("The call addn(", val, ") returns", addn(val))
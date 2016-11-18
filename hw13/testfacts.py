def factorial(arg):
  arg = int(arg)
  if arg > 1:
    return arg * factorial(arg-1)
  else:
    return arg

# userinput = input("What do you want to factorial?\n")
# Commented out user input capabilities
userinput = 10
print(factorial(userinput))
def factorial(arg):
  if arg > 0:
    return arg * factorial(arg-1)
  else:
    return 1



userinput = 1
while True:
  if userinput != 0:
    userinput = input("Enter a number you want the factorial of (0 to exit): \n\n\n")
    print("n --------------- factorial(n)\n%s                    %s") %(userinput, factorial(userinput))

    # print("n --------------- factorial(n)\n")
    # print("%s") %(userinput)
    # print("                    ")
    # print(factorial(userinput))
  else:
    break


# Once the user the factorial loop, it will display the square roots from 0 to 6
print("You exited the factorial loop, but here is the original FOR LOOP, which will run all the factorials from 0 to your number\n")
userinput = input("Enter a number you want the factorial of (will exit after displaying the factorials)\n")
print("n --------------- factorial(n)")
for n in range(1, userinput+1):
    print("%s \t\t    %s") %(n, factorial(n))
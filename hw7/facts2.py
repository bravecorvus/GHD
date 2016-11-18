def factorial(arg):
  if int(arg) > 0:
    return arg * factorial(arg-1)
  else:
    return 1



userinput = 1
while True:
  if userinput != 0:
    userinput = int(input("Enter a number you want the factorial of (0 to exit): \n\n\n"))
    print("n --------------- factorial(n)")
    print(userinput)
    print(factorial(userinput))
  else:
    break


# Once the user the factorial loop, it will display the square roots from 0 to 6
print("You exited the factorial loop, but here is the original FOR LOOP, which will run all the factorials from 0 to your number\n")

print("n --------------- factorial(n)")
n = 1
userinput = input("Enter a number you want the factorial of (will exit after displaying the factorials)\n")


while n < int(userinput)+1:
    print (str(n), "              ", str(factorial(n)))
    n=n+1
    ++n
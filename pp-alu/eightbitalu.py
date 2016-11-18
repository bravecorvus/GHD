#Eight Bit Adder Functionality (Well, 8 bit to 64 bit)
#Retains the majority of the functionality from the original classless ALU program (aluImperative.py), but adds some non-imperative code in order to allow for user control of the ALU
#Ability to take in a user defined input, A + B, (A and B being base 10 integers) compute it (while giving the user feedback at the various steps as well as the values in base 2 binary representation), and finally the final output back in base 10 integer form.
#At first glance, it seems alot easier to implement the 8 bit ALU using the ALU class I defined in alu.py, but...
#Talking with Prof Brown, he made it seem like I would get more extra credit if I used the imperative original code to construct 8-bit ALU's so thats what i did
import blogic
from blogic import *


def decoder(f_0,f_1): #arg = control lines F0 and F1 #return = a tuple with 4 lines corresponding to what needs to be done at the moment
        return(band(bnot(f_0), bnot(f_1)), band(bnot(f_0), f_1), band(f_0, bnot(f_1)), band(f_0, f_1))

def logical_unit(a, b, f_0, f_1): #args = values of a, and b, as well as the control lines F0, and F1 #return = value used for direct output and full adder using
    return bor(band(band(a, b), decoder(f_0,f_1)[0]),band(bor(a,b), decoder(f_0,f_1)[1]),band(bnot(b), decoder(f_0,f_1)[2]))

def fulladder(a, b, f, carryIn): #args= values of A, B, and the decoded passed variable (from F0, and F1), and the carry in #return = purely the output of the Fuller Adder.
    return band(bxor(carryIn, bxor(a,b)),f)

def carryOut(a,b,f, carryIn): #args = values of A, B, and the decoded passed variable f (from F0, and F1) as well as the carryIn value passed from determineCarry() #return the value of the carry out
    return bor(band(f, a, b),band(f, bxor(a,b), carryIn))

def determine_a(ena, a, inva): #using variables Enable A (ena), A, and Invert A (inva), this function returns the value past A's XOR gate in the ALU circuit chart on pg 167
    return bxor(inva, band(a, ena))

def determine_b(enb, b):#using variables Enable B (enb), A, and B, this function returns the value past B's AND gate in the ALU circuit chart on pg 167
    return band(b, enb)

def determineOutput(f_0, f_1, inva, ena, enb, carry, a, b): #Utilizing the various helper functions that mirror the ALU's Control Lines, input variables, Logical Unit, Decoder, Carry In, and Full Adder, this function calculates the output of the ALU.
# However, carry out is not determined at this time
    return bor(logical_unit(determine_a(ena, a, inva),determine_b(enb, b),f_0, f_1), fulladder(determine_a(ena, a, inva), determine_b(enb, b), decoder(f_0, f_1)[3], carry))


def determineCarry(f_0, f_1, inva, ena, enb, carry, a, b): #Parent function of carryOut, sets up correct a, b, and f variables using the determine_a(), determine_b(), and decoder() functions, before passing it to carryOut() along with variable carry
    return carryOut(determine_a(ena, a, inva),determine_b(enb, b), decoder(f_0, f_1)[3], carry)

def alu(f_0, f_1, inva, ena, enb, carry, a, b): #Overarching function that ties all the different parts of the ALU together. Calls helper function determine Output
    return(determineOutput(f_0, f_1, inva, ena, enb, carry, a, b))


def print_call(f_0, f_1, inva, ena, enb, carry, a, b): # Not used in this program. Look in aluImperative.py
    print("alu", str(f_0), str(f_1), str(inva), str(ena), str(enb), str(carry), str(a), str(b), " --> ", str(alu(f_0, f_1, inva, ena, enb, carry, a, b)))

def print_section(f_0, f_1, inva, ena, enb): # Not used in this program. Look in aluImperative.py
    print("F0=" + str(f_0), end=" , ")
    print("F1=" + str(f_1), end=" , ")
    print("inva=" + str(inva), end= " , ")
    print("ena=" + str(ena), end=" , ")
    print("enb=" + str(enb))
    for carry in range(2):
        for a in range(2):
            for b in range(2):
                print_call(f_0, f_1, inva, ena, enb, carry, a, b)

def fullPrint(): # Not used in this program. Look in aluImperative.py
    for f_0 in range(2):
        for f_1 in range(2):
            for inva in range(2):
                for ena in range(2):
                    for enb in range(2):
                        print_section(f_0, f_1, inva, ena, enb)





###Up until this point, I only used Imperative Methods
# From here, since I will get 2 integer values from the user, which needs to go through some conversions, it will be less imperative


# The standard fixformatting() function
# It will return the fixed length of the list in powers of two
#It is meant to be a first run through. A second pass is needed in order to correct discrepancies between fixed a and fixed b
def fixformatting(arg): #takes in a base 10 integer user input
    bindata = list(bin(arg)[2:]) #converts the base 10 integer into a list of binary values
    fixlen = 8 - len(bindata) #Computes the discrepancy of the binary value of the value and the 8 bit value
    if fixlen < 0: # If the data overflows in an 8 bit ALU, we will make a 16 bit ALU
        fixlen = 16 - len(bindata)
    elif fixlen < 0: # If the data overflows in an 16 bit ALU, we will make a 32 bit ALU
        fixlen = 32 - len(bindata)
    elif fixlen < 0: # If the data overflows in an 32 bit ALU, we will make a 64 bit
        fixlen = 64 - len(bindata)
    for i in range(0, fixlen):# pad the head of the list with 0's until the desired length is reached. The desired length is determined by the variable fixlen
        bindata.insert(0, 0)
    
    for count, data in enumerate(bindata): #convert the various values into integers
        bindata[count] = int(data) #NOTE: Will not affect the values if they are already an integer
    return bindata #Returns the reformatted list

# If A, and B have different lengths after going through fixformatting, this function pads 0's onto the head of the smaller list until it is the same length as the larger list
def fixdiscrepancy(arg, difference): #takes in a base 10 integer user input
    for i in range(0, difference):#Since difference between the length of A list and the length of B list is directly passed as difference, we can use as the iteration guard
        arg.insert(0, "0") 
    for count, data in enumerate(bindata):
        arg[count] = int(data) #Note, this function directly edits the original list for performance purposes.




userinput = input("Give me a integer, an operator, and an integer to compute using my procedural ALU program\n(e.g. '55 + 167')\n(NOTE: INCLUDE SPACE IN BETWEEN A, OPERATOR, AND B\n")
#e.g. 100 + 100
input_list = userinput.split(' ')# Splits the list by spacing into a 3 element list, such that input_list will look like [VariableA, Operator, VariableB] all in string format
a = fixformatting(int(input_list[0])) #Since in the input 100 + 40, 100 is the first element of the list, we pass it using input_list[0], convert into int, and pad the 0's accordingly
b = fixformatting(int(input_list[2])) #Since in the input 100 + 40, 40 is the last element of the list, we pass it using input_list[2], convert into int, and pad the 0's accordingly
discrepancy = len(a) - len(b) #Since there is no guarantee the user entered 2 numbers that can be represented by the same number of binary digits, we will make sure the length are the same
if discrepancy != 0: #If the length are not the same, determine which value is smaller, and pass that through fixdiscrepancy along with the difference in length with the longer list in order have A and B at the same length
    if discrepancy < 0: #If length of A - lenth of B yeilded a negative number, it means the A list was a smaller list
        fixdiscrepancy(b, (-1)*discrepancy) #Note: Multiply -1 to the difference because we will use it as an iteration variable
    elif discrepancy > 0: #If length of A - length of B yielded a positive number, it means B was smaller, and we pass that through fixdiscrepancy() in a similar fashion
        fixdiscrepancy(a, discrepancy)
print("The Binary Representation of A is " + ''.join([str(i) for i in a])+" and "+str(len(a))+" bits were necessary to represent it\n") #Just printing out the Binary representation of A
print("The Binary Representation of B is " + ''.join([str(i) for i in b])+" and "+str(len(a))+" bits were necessary to represent it\n") #Just printing out the Binary representation of B

output = []
if input_list[1] == "+": #If you wanted addition of A and B
    lastcarry = 0 #lastcarry represents the most recent carry out value, which will be going in as the carry in value for the iteration. Although not purely imperative, it was necessary because I needed a way to pipe the carry out into the carry in
    for count, data in reversed(list(enumerate(a))):
        output.insert(0, alu(1, 1, 0, 1, 1, lastcarry, a[count], b[count])) #insert(0, blahblahblah) will basically list.append() a tthe head rather than at the tail
        lastcarry = determineCarry(1, 1, 0, 1, 1, lastcarry, a[count], b[count]) #Setting lastcarry is done last since it the a variable we will use in the next iteration
elif input_list[1] == "-": #If you wanted subtraction of A and B
    for i in b:
        i = bnot(i) #flipping bits as is the standard in 2's compliment subtraction
    lastcarry = 0 #lastcarry represents the most recent carry out value, which will be going in as the carry in value for the iteration
    for count, data in reversed(list(enumerate(a))):
        output.insert(0, alu(1, 1, 0, 1, 1, lastcarry, a[count], b[count]))
        lastcarry = determineCarry(1, 1, 1, 1, 1, lastcarry, a[count], b[count])

cut = 0 #Cut is the number of empty 0's in the beginnning of the final output binary list.
for count, data in enumerate(output): #This for loop counts the amount of 0's in the front we have in the head of the list
    if output[count] != 0: #As soon as you hit a value other than 0 (namely 1), set cut to the current iteration integer value, and break out of the loop
        cut = count
        break

del output[0:cut] #remove the empty 0's from the beginning of the list
print("The Binary Representation of the Resulting 8 bit ALU Operation is " + ''.join([str(i) for i in output])+" and "+str(len(output))+" bits were necessary to represent it\n")

outputstring = ''.join([str(i) for i in output]) #concatenates the list back into string form.
print("Integer Representation of Final Output "+str(int(outputstring, 2))) #converting back into base 10 integer, then string.
                                                #^^Cutting the 0's out of the output list is crucial because without it,
                                                #Python will refuse to convert back to base 10 integer representation
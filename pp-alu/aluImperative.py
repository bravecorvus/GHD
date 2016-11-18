#Fully project compliant Program
#Not very fun, but it gets the job done
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


def print_call(f_0, f_1, inva, ena, enb, carry, a, b): #prints each line the alu values, but not the F0 = ... line at the top
    print("alu", str(f_0), str(f_1), str(inva), str(ena), str(enb), str(carry), str(a), str(b), " --> ", str(alu(f_0, f_1, inva, ena, enb, carry, a, b)))

def print_section(f_0, f_1, inva, ena, enb): #prints the basic F0, F1, inva, ENA, and ENB variables at the top
    print("F0=" + str(f_0), end=" , ")
    print("F1=" + str(f_1), end=" , ")
    print("INVA=" + str(inva), end= " , ")
    print("ENA=" + str(ena), end=" , ")
    print("ENB=" + str(enb))
    for carry in range(2):
        for a in range(2):
            for b in range(2):
                print_call(f_0, f_1, inva, ena, enb, carry, a, b)

def fullPrint(): #Used to print the "complete 32 element" ALU list, but not user defined ALU objects.
    for f_0 in range(2):
        for f_1 in range(2):
            for inva in range(2):
                for ena in range(2):
                    for enb in range(2):
                        print_section(f_0, f_1, inva, ena, enb)

# int main() {
fullPrint() 
# }
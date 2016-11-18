powersoftwo = [1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024, 2048, 4096]
paritypositions = [0, 1, 3, 7, 15, 31, 63, 217, 255, 511, 1023, 2047, 4095]


def parity(arg):
    counter = 0
    for count, data in enumerate(arg):
        counter += int(data)
    # print("Mod 2 is ", counter%2)
    return counter%2

def sublist(binlist, paritynumber):
    counterofbinlist = paritynumber-1
    sublist = [] #creating my sublist
    testcounter = 1
    binlist[paritynumber-1] = 0
    while counterofbinlist < len(binlist):
        # print("Counter of Bin =", counterofbinlist, "During", testcounter, "st iteration")
        upperbound = counterofbinlist + paritynumber
        # Leftover digits that need to be calculated that kind of go off to the right of the binary
        if upperbound <= len(binlist):
            # print("Upperbound =", upperbound, "During", testcounter, "st iteration")
            sublist.extend(binlist[counterofbinlist:upperbound])
            # print("Sublist", sublist, "During", testcounter, "st iteration")
            counterofbinlist = upperbound + paritynumber
            # print("Counter of Binary List", counterofbinlist, "During", testcounter, "st iteration")
            testcounter += 1
            # print("\n\n")
        else:
            sublist.extend(binlist[counterofbinlist:])
            break
    # print("Sublist length is ", len(sublist))
    return parity(sublist)

# Identical to above, but does not SET the parity bit because we are trying to check if an encoding is correct, not setting up the encoding
# Also not passing it directly to method parity since we have a different purpose
def sublist2(positionlist, binlist, paritynumber):
    counterofbinlist = paritynumber-1
    sublist = [] #creating my sublist
    testcounter = 1
    while counterofbinlist < len(binlist):
        # print("Counter of Bin =", counterofbinlist, "During", testcounter, "st iteration")
        upperbound = counterofbinlist + paritynumber
        # print("Upperbound =", upperbound, "During", testcounter, "st iteration")
        if upperbound <= len(binlist):
            sublist.extend(positionlist[counterofbinlist:upperbound])
            # print("Sublist", sublist, "During", testcounter, "st iteration")
            counterofbinlist = upperbound + paritynumber
            # print("Counter of Binary List", counterofbinlist, "During", testcounter, "st iteration")
            testcounter += 1
            # print("\n\n")
    # print("Sublist length is ", len(sublist))
        else:
            sublist.extend(positionlist[counterofbinlist:])
            break
    return sublist




def noparitybits(arglist):
    returnlist = []
    for count, data in enumerate(arglist):
        if count not in paritypositions:
            temp = int(data)
            returnlist.append(temp)
    return returnlist

def onlyparitybits(arglist):
    returnlist = []
    for count, data in enumerate(arglist):
        if count in paritypositions:
            temp = int(data)
            returnlist.append(temp)
    return returnlist


# for reformatting the data to have enough digits such that they will always be a power of 2
def fixformatting(arg):
    bindata = list(bin(arg)[2:])
    fixlen = 0
    # need to fix the length of the set in powers of two
    if len(bindata) > 2 and len(bindata) < 4:
        fixlen = 4 - len(bindata)
    elif len(bindata) > 4 and len(bindata) < 8:
        fixlen = 8 - len(bindata)
    elif len(bindata) > 8 and len(bindata) < 16:
        fixlen = 16 - len(bindata)
    elif len(bindata) > 16 and len(bindata) < 32:
        fixlen = 32 - len(bindata)
    elif len(bindata) > 32 and len(bindata) < 64:
        fixlen = 64 - len(bindata)
    elif len(bindata) > 64 and len(bindata) < 128:
        fixlen = 128 - len(bindata)
    elif len(bindata) > 128 and len(bindata) < 256:
        fixlen = 256 - len(bindata)
    elif len(bindata) > 256 and len(bindata) < 1024:
        fixlen = 1024 - len(bindata)
    elif len(bindata) > 1024 and len(bindata) < 2048:
        fixlen = 2048 - len(bindata)
    elif len(bindata) > 2048 and len(bindata) < 4096:
        fixlen = 4096 - len(bindata)
    if fixlen > 0:
        for i in range(0, fixlen):
            bindata.insert(0, 0)
    return bindata






def hamming (userinput):
    bindata = fixformatting(userinput)

    # print("Original bindata", bindata)
    for counter, data in enumerate(powersoftwo):
        # if statement to make sure the counter doesn't overflow the length of the powersoftwolist
        if counter+1 < len(powersoftwo):
            # lower bound
            n1 = powersoftwo[counter]
            #upper bound
            n2 = powersoftwo[counter+1]
            x = len(bindata)
            # if the length of the binary list falls between the lower bound and the upper bound, set the number of parity bits as iteration variable + 1
            if x >= n1 and x <= n2:
                numofparitybits = counter+1
    hamminglist = [0] * (len(bindata) + numofparitybits) #length = length of arg in binary + number of necessary hamming codes
    # 0 is just a arbitrary number to populate the list
    # temporarily enter the varity bits in the list with the string "parity".
    
    # a loop which checks to see the length of binary list. and outputs the position of the list as the number of parity bits
    # when there is a match such that list_element <= length of the binary number <= next list list_element

    # fills out the string "parity" every time it matches up with the powers of two table
    for x in powersoftwo:
        if x <= len(hamminglist):
            hamminglist[x-1] = "parity"
    bindatacounter = 0 #need a separate counter to count through the binary list since the added parity bits of the new list would mess up the count
    # fills up all other values
    for counter, data in enumerate(hamminglist):
        if data != "parity": #whole point of entering parity in the earlier loop
            hamminglist[counter] = int(bindata[bindatacounter])
            bindatacounter += 1 #throw this in the if statement so the indexing counter we use for the bindata list will not be +1'ed if the hammingcode 
            # content  at the counter is a parity bit
    # replace every string parity with the equivalent parity throught the method sublist
    for counter, data in enumerate(hamminglist):
        if data == "parity":
            hamminglist[counter] = sublist(hamminglist, counter+1)
    hamstring = ''.join([str(i) for i in hamminglist])
    finalint = int(hamstring, 2)
    return hex(finalint)


def errorfixing(stringarg):
    hammingcode = []
    # converts the string into a list
    hammingcode.extend(stringarg)
    # find where how many parity bits are in the hamming code
    if len(hammingcode) == 1:
        paritybits = 1
    elif len(hammingcode) > 2 and len(hammingcode) < 4:
        paritybits = 2
    elif len(hammingcode) > 3 and len(hammingcode) <= 7:
        paritybits = 3
    elif len(hammingcode) > 7 and len(hammingcode) <= 15:
        paritybits = 4
    elif len(hammingcode) > 15 and len(hammingcode) <= 31:
        paritybits = 5
    elif len(hammingcode) > 31 and len(hammingcode) <= 63:
        paritybits = 6
    elif len(hammingcode) > 63 and len(hammingcode) <= 127:
        paritybits = 7
    elif len(hammingcode) > 127 and len(hammingcode) <= 255:
        paritybits = 8
    elif len(hammingcode) > 255 and len(hammingcode) <= 511:
        paritybits = 9
        # Theoretically, I should hardcode a larger amount, but I'm not going to



    # Creating a full list of the indexes of paritypositions so we can reference them later
    hamcodepositions = []
    for counter, data in enumerate(hammingcode):
        if counter < len(hammingcode):
            hamcodepositions.append(counter)

    # the following constructs a list which tracks everywhere we have an error in the parity bit
    errorloglists = []
    # using the paritypositions list at the top, we iterate through every spot there is a parity bit
    paritypositionssublist = paritypositions[:paritybits]
    for counter, data in enumerate(paritypositionssublist):
        if paritypositionssublist[counter] <= len(hammingcode):
            paritychecklist = sublist2(hamcodepositions, hammingcode, data+1)
            # because having multiple lists of 0's and 1's is useless to compare among one another, we set the paritychecklist as the positions of those elements
            parityvaluelist = []
            # Need a value list to actually find the parity
            for i in paritychecklist:
                parityvaluelist.append(int(hammingcode[i]))
                # if the parity of the sublist of say take one skip one take one skip one is not equal to the first parity bit, then add it to the errorloglist
            if int(hammingcode[data]) == parity(parityvaluelist):
                # The stucture are lists within lists
                errorloglists.append(paritychecklist)
            print("Parity Value's List", parityvaluelist)
            print("Parity Check List", paritychecklist)
            print("Value of the argument parity bit", hammingcode[data])
            print("Value of the parity of the actual sub-list", parity(parityvaluelist))
            print("\n\n")
    # print(errorloglists)

    # Now, going through the errorloglist, we go through and search for any value in hamcodepositions that aren't found anywhere
    # because of the nature of how Hamming Codes work, this will give us the error location (assuming that there is only one error)
    errorcodeposition = hamcodepositions
    notinoneiteration = []
    for counter, data in enumerate(errorloglists):
        
        # removing the parity bit
        del data[0]
        for counter2, data2 in enumerate(hamcodepositions):
            if data2 not in data:
                notinoneiteration.append(data2)
        for counter3, data3 in enumerate(notinoneiteration):
            if data3 in data:
                notinoneiteration.remove(data3)
    locationoferror = 0
    for i in errorloglists:
        print(i)
        # locationoferror += i

    print("The error is located in ", locationoferror-1)
    print("It should be", (1 + int(hammingcode[locationoferror-1]))%2)
    print("instead of", hammingcode[locationoferror-1])


# int main
# userinput = input("Pick a hex value you want to evaluate the hamming code for\n")
#It can take the hex form 0x..... or .....
if userinput[:2] == "0x":
    userinput = userinput[2:]
encodedhexstring = hex(int(hamming(int(userinput, 16)), 16))
strippedhexstring = encodedhexstring[2:]
print("The hamming code is ", strippedhexstring)
# userinput = input("What number do you want to check for bit errors?")
# e.g. 001101000010001011101
# errorfixing(userinput)
# errorfixing("101000001010")




#Disclaimers: I initially attempted to implement a method using bit shift operators, but I got overwhelemed and I gave up.
# My hamming method splits the process into multiple distinct parts.
# 1) Retreive the hexidecimal list and turn it into a binary form list
# 2) Using a list with the powers of two, it figures out how many parity bits this calculation will need.
# 3) Then it creates a new list of length original list + the amount of parity bits needed with 0's
# 4) It fills up just the spots for the parity bits with the string "parity" to be able to distinguish from normal bits
# 5) It fills out the rest of the values based on the original values of the user inputted binary number
# 6) It uses the method sublist which takes in the hamminglist, and the value of the current parity bit relative to the powers of two list. Based on this value, it 
        #creates a sublist of the bits the program needs to check (including the parity bit itself which is passed as a 0 so as not to affect the parity of the operation)
        #Once it creates the sublist, it passes the sublist into a method parity which computes the parity of all the numbers by adding them all up and taking %2.

# 7) The value of this replaces the original value of "parity" in the hamminglist
# 8) At the end, the int list consisting of 1's and 0's is converted into a string, then an int base 2 (binary), then a hexidecimal again to return to the function call
# 9) The function call is called within a print function, and the value of the userinput with the encoded hamming code is returned as a hexidecimal.
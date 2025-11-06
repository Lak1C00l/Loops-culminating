"""
Lara Atanasova

Conditionals and loops assignment

Converting type of Binary to number system

Level 4
"""

convertedNum = 0
#convertedNumIntPart = 0
convertedNumRemPart = 0
storedConvertedNums = []
storedConvertedNumsWithPluses = []
numberInSystem = 0
numberSystem = ""
finalNumSysToInt = 0
remDivRes = 0

#function that converts number system to decimal and stores values in lists for later augmentation
def calculateNumberSystemToDecimal(numInPlaceVal : int, numberToSquareBy : int, count : int):
    convertedNum = numInPlaceVal*numberToSquareBy**count
    print(f'{numInPlaceVal} x {numberToSquareBy}^{count} = {convertedNum}')
    storedConvertedNums.append(convertedNum)
    storedConvertedNumsWithPluses.append(str(convertedNum))
    storedConvertedNumsWithPluses.append("+")


#function that does conversion from decimal to number system and returns the integer value for while loops (otherwise it gets overided by the global variable for some reason)
def calculateDecimalToNumberSystem(numInPlaceVal : int, numberToDivBy : int):
    convertedNumIntPart = numInPlaceVal//numberToDivBy
    convertedNumRemPart = numInPlaceVal % numberToDivBy
    print(f'{numInPlaceVal} // {numberToDivBy} = {convertedNumIntPart}')
    print(f'{numInPlaceVal} % {numberToDivBy} = {convertedNumRemPart}')
    storedConvertedNums.append(convertedNumRemPart)

    return convertedNumIntPart;

#function to print the result of number system to decimal conversion
def printingOfResultsNumSysToInt():
    storedConvertedNumsWithPluses.pop()
    print(storedConvertedNumsWithPluses)
    print(f"= {finalNumSysToInt}")


notValidInput = True;
while notValidInput:
    # user identifies whether they want to convert from decimal to another number system or from another number system to decimal 
    typeOfConversion = input("Would you like to convert from decimal to a number system(1) or from a number system to decimal(2)? :  ")
    
    #validate if user input is either one or two 
    if typeOfConversion == "1" or typeOfConversion == "2":
        #valid conversion = false
        notValidInput = False;
    else:
        print(f"The charachter you entered : '{typeOfConversion}' is not a valid input. Try again.")


#code executes if user wants to convert from decimal to number system
if typeOfConversion == "1":
    # gets specific number that use would like to convert
    decimal = int(input("What decimal would you like to convert? : "))
    #gets number system that user wants to convert to
    numberSystem = int(input("Please type your number system's base amount of unique numbers (2-9) or 16? : "))

    convertedNumIntPart = decimal
    # if hexadecimal than replace all remainders with corresponding letter
    if numberSystem == 16:
         while convertedNumIntPart > 0:
            #first dose calculation and stores variable
            convertedNumIntPart = calculateDecimalToNumberSystem(convertedNumIntPart, numberSystem)


            #changes value if remainder is from 10-15 with right letter and prints step
            if 10 in storedConvertedNums:
                storedConvertedNums.pop()
                storedConvertedNums.append("A")
                print("In hexadecimal A = 10")
                print(storedConvertedNums)
            elif 11 in storedConvertedNums:
                storedConvertedNums.pop()
                storedConvertedNums.append("B")
                print("In hexadecimal B = 11")
                print(storedConvertedNums)
            elif 12 in storedConvertedNums:
                storedConvertedNums.pop()
                storedConvertedNums.append("C")
                print("In hexadecimal C = 12")
                print(storedConvertedNums)
            elif 13 in storedConvertedNums:
                storedConvertedNums.pop()
                storedConvertedNums.append("D")
                print("In hexadecimal D = 13")
                print(storedConvertedNums)
            elif 14 in storedConvertedNums:
                storedConvertedNums.pop()
                storedConvertedNums.append("E")
                print("In hexadecimal E = 14")
                print(storedConvertedNums)
            elif 15 in storedConvertedNums:
                storedConvertedNums.pop()
                storedConvertedNums.append("F")
                print("In hexadecimal F = 15")
                print(storedConvertedNums)

    #if number system is other than do normal calculations
    else:
        while convertedNumIntPart > 0:
            convertedNumIntPart = calculateDecimalToNumberSystem(convertedNumIntPart, numberSystem)
            print(storedConvertedNums)
        
    # print final value
    storedConvertedNums.reverse()
    print(f"Final resulting number is: {storedConvertedNums}")

#code executes if user wants to convert from number system to decimal
elif typeOfConversion == "2":
    # checking which number system user wants to convert from
    numberSystem = int(input("Please type your number system's base amount of unique numbers (1-9) or 16? : ").lower())

    # if number system is hexadecimal than store input as string
    if numberSystem == 16:
        numberInSystem = input("What Hexadecimal would you like to convert? : ").lower()
    # but if number system is between and including 1-9 than store input as int
    elif numberSystem <= 9 or numberSystem >= 1:
        numberInSystem = int(input("What number in your number system would you like to convert from? : "))

    # BINARY
    if numberSystem == 2:
        #If user types a number that cannot be a binary number than throw error until user inputs a number within binary parameters
        while str(numberInSystem).find("2")>-1 or str(numberInSystem).find("3")>-1 or str(numberInSystem).find("4")>-1 or str(numberInSystem).find("5")>-1 or str(numberInSystem).find("6")>-1 or str(numberInSystem).find("7")>-1 or str(numberInSystem).find("8")>-1 or str(numberInSystem).find("9")>-1  :
            print("A binary number only has ones and zeros")
            numberInSystem = int(input("Please type a number only with ones and zeros: "))

        #splitting the input into a list so that each individual digit can be converted on its own
        numberInSystem = [int(x) for x in str(numberInSystem)]

        #count increases each iteration because it is the place value of the current digit that is being calculated
        count = 0

        #Loop to do calculation for entire binary number
        for i in reversed(numberInSystem):
            calculateNumberSystemToDecimal(i,2,count)
            count+=1
        #Loop to add all calculated numbers
        for i in storedConvertedNums:
            finalNumSysToInt += i
        #printing final value
        printingOfResultsNumSysToInt()

    # TERNARY
    elif numberSystem == 3:
        #If user types a number that cannot be a ternary number than throw error until user inputs a number within ternary parameters
        while str(numberInSystem).find("3")>-1 or str(numberInSystem).find("4")>-1 or str(numberInSystem).find("5")>-1 or str(numberInSystem).find("6")>-1 or str(numberInSystem).find("7")>-1 or str(numberInSystem).find("8")>-1 or str(numberInSystem).find("9")>-1  :
            print("A ternary number only contains numbers within 0-2")
            numberInSystem = int(input("Please type a number only with 0-2s: "))

        #splitting the input into a list so that each individual digit can be converted on its own
        numberInSystem = [int(x) for x in str(numberInSystem)]

        #count increases each iteration because it is the place value of the current digit that is being calculated
        count = 0

        #Loop to do calculation for entire ternary number
        for i in reversed(numberInSystem):
            calculateNumberSystemToDecimal(i,3,count)
            count += 1
        #Loop to add all calculated numbers
        for i in storedConvertedNums:
            finalNumSysToInt += i
        #printing final value
        printingOfResultsNumSysToInt()

    # Quaternary
    elif numberSystem == 4:
         #If user types a number that cannot be a quaternary number than throw error until user inputs a number within quaternary parameters
        while str(numberInSystem).find("4")>-1 or str(numberInSystem).find("5")>-1 or str(numberInSystem).find("6")>-1 or str(numberInSystem).find("7")>-1 or str(numberInSystem).find("8")>-1 or str(numberInSystem).find("9")>-1  :
            print("A quaternary number only contains numbers within 0-3")
            numberInSystem = int(input("Please type a number only with 0-3s: "))

        #splitting the input into a list so that each individual digit can be converted on its own
        numberInSystem = [int(x) for x in str(numberInSystem)]

        #count increases each iteration because it is the place value of the current digit that is being calculated
        count = 0

        #Loop to do calculation for entire Quaternary number
        for i in reversed(numberInSystem):
            calculateNumberSystemToDecimal(i,4,count)
            count += 1
        #Loop to add all calculated numbers together
        for i in storedConvertedNums:
            finalNumSysToInt += i
        #printing final value
        printingOfResultsNumSysToInt()

    #  QUINARY
    elif numberSystem == 5:
        #If user types a number that cannot be a quinary number than throw error until user inputs a number within quinary parameters
        while str(numberInSystem).find("5")>-1 or str(numberInSystem).find("6")>-1 or str(numberInSystem).find("7")>-1 or str(numberInSystem).find("8")>-1 or str(numberInSystem).find("9")>-1  :
            print("A quinary number only contains numbers within 0-4")
            numberInSystem = int(input("Please type a number only with 0-4s: "))

        #splitting the input into a list so that each individual digit can be converted on its own
        numberInSystem = [int(x) for x in str(numberInSystem)]

        #count increases each iteration because it is the place value of the current digit that is being calculated
        count = 0

        #Loop to do calculation for entire quinary number
        for i in reversed(numberInSystem):
            calculateNumberSystemToDecimal(i,5,count)
            count += 1
        #Loop to add all calculated numbers together
        for i in storedConvertedNums:
            finalNumSysToInt += i
         #printing final value
        printingOfResultsNumSysToInt()

    # SENARY
    elif numberSystem == 6:
        #If user types a number that cannot be a senary number than throw error until user inputs a number within senary parameters
        while str(numberInSystem).find("6")>-1 or str(numberInSystem).find("7")>-1 or str(numberInSystem).find("8")>-1 or str(numberInSystem).find("9")>-1  :
            print("A senary number only contains numbers within 0-5")
            numberInSystem = int(input("Please type a number only with 0-5s: "))

        #splitting the input into a list so that each individual digit can be converted on its own
        numberInSystem = [int(x) for x in str(numberInSystem)]

        count = 0

        #Loop to do calculation for entire senary number
        for i in reversed(numberInSystem):
            calculateNumberSystemToDecimal(i,6,count)
            #count increases each iteration because it is the place value of the current digit that is being calculated
            count += 1
        #Loop to add all calculated numbers together
        for i in storedConvertedNums:
            finalNumSysToInt += i
        #printing final value
        printingOfResultsNumSysToInt()

    # septenary
    elif numberSystem == 7:
        #If user types a number that cannot be a septenary number than throw error until user inputs a number within septenary parameters
        while str(numberInSystem).find("7")>-1 or str(numberInSystem).find("8")>-1 or str(numberInSystem).find("9")>-1  :
            print("A senary number only contains numbers within 0-6")
            numberInSystem = int(input("Please type a number only with 0-6s: "))

        #splitting the input into a list so that each individual digit can be converted on its own
        numberInSystem = [int(x) for x in str(numberInSystem)]

        count = 0
        #Loop to do calculation for entire septenary number
        for i in reversed(numberInSystem):
            calculateNumberSystemToDecimal(i,7,count)
            count += 1 #count increases each iteration because it is the place value of the current digit that is being calculated
        #Loop to add all calculated numbers together
        for i in storedConvertedNums:
            finalNumSysToInt += i
        #printing final value
        printingOfResultsNumSysToInt()

    # OCTAL
    elif numberSystem == 8:
        #If user types a number that cannot be an octal number than throw error until user inputs a number within octal parameters
        while  str(numberInSystem).find("8")>-1 or str(numberInSystem).find("9")>-1  :
            print("An octal number only contains numbers within 0-7")
            numberInSystem = int(input("Please type a number only with 0-7s: "))

        #splitting the input into a list so that each individual digit can be converted on its own
        numberInSystem = [int(x) for x in str(numberInSystem)]

        count = 0
          #Loop to do calculation for entire octal number
        for i in reversed(numberInSystem):
            calculateNumberSystemToDecimal(i,8,count)
            count += 1#count increases each iteration because it is the place value of the current digit that is being calculated
        #Loop to add all calculated numbers together
        for i in storedConvertedNums:
            finalNumSysToInt += i
        #printing final value
        printingOfResultsNumSysToInt()

    # NONAL
    elif numberSystem == 9:
        #If user types a number that cannot be a nonal number than throw error until user inputs a number within octal parameters
        while  str(numberInSystem).find("9")>-1  :
            print("An octal number only contains numbers within 0-8")
            numberInSystem = int(input("Please type a number only with 0-8s: "))
        
        #splitting the input into a list so that each individual digit can be converted on its own
        numberInSystem = [int(x) for x in str(numberInSystem)]
        count = 0
        #Loop to do calculation for entire nonal number
        for i in reversed(numberInSystem):
            calculateNumberSystemToDecimal(i,9,count)
            count += 1 #count increases each iteration because it is the place value of the current digit that is being calculated
         #Loop to add all calculated numbers together
        for i in storedConvertedNums:
            finalNumSysToInt += i
        #printing final value
        printingOfResultsNumSysToInt()

    # HEXADECiMAIL
    elif numberSystem == 16:
        #If user types a number that cannot be a nonal number than throw error until user inputs a number within hexadecimal parameters
        while  not( numberInSystem.find("0")>-1 or numberInSystem.find("1")>-1 or numberInSystem.find("2")>-1 or numberInSystem.find("3")>-1 or numberInSystem.find("4")>-1 or numberInSystem.find("5")>-1 or numberInSystem.find("6")>-1 or numberInSystem.find("7")>-1 or numberInSystem.find("8")>-1 or numberInSystem.find("9")>-1  )      or       not(numberInSystem.find("a")>-1 or numberInSystem.find("b")>-1 or numberInSystem.find("c")>-1 or numberInSystem.find("e") or numberInSystem.find("f") ):
            print("A hexadecimal number only contains numbers within 0-9 and A-F")
            numberInSystem = input("Please type a number only with 0-9s and A-F's: ").lower()

        count = 0

        #splitting the input into a list so that each individual digit can be converted on its own
        numberInSystem = [str(x) for x in str(numberInSystem)]

        # Here the loop to do the conversion is modified since in a hexadecimal not all it's digits are base 10 digits. 
        # If the user's hexadecimal digit contains a letter than the loop identifies what letter within the allowed parameters it is and executes the function to calculate with the letter's value replaced by it's corresponding base ten value 
        for i in reversed(numberInSystem):
            if i.find("a")>-1: 
                calculateNumberSystemToDecimal(10, 16, count)
            elif i.find("b")>-1:
                calculateNumberSystemToDecimal(11,16,count)
            elif i.find("c")>-1:
                calculateNumberSystemToDecimal(12,16,count)
            elif i.find("d")>-1:
                calculateNumberSystemToDecimal(13,16,count)
            elif i.find("e")>-1:
                calculateNumberSystemToDecimal(14,16,count)
            elif i.find("f")>-1:
                calculateNumberSystemToDecimal(15,16,count)
            # Otherwise if the selected digit within the hexadecimal is not a letter than execute the regular code to convert with the digit being i
            else:
                calculateNumberSystemToDecimal(int(i),16,count)
            #count increases after each iteration because it is the place value of the current digit that is being calculated
            count += 1
        #Adding together each digit's calculated value to get our reult as an integer
        for i in storedConvertedNums:
            finalNumSysToInt += i
         #printing final value
        printingOfResultsNumSysToInt()
    # This executes if the user enetrs the value of a number system that cannot be calculated in this code
    else:
        print(f"{numberSystem} number system dose not exist or is not a convertable option.")
        numberSystem = input("Try another number system to convert from: ").lower()


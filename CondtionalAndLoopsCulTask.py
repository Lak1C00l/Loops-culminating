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

def calculateNumberSystemToDecimal(numInPlaceVal : int, numberToSquareBy : int, count : int):
    convertedNum = numInPlaceVal*numberToSquareBy**count
    print(f'{numInPlaceVal} x {numberToSquareBy}^{count} = {convertedNum}')
    storedConvertedNums.append(convertedNum)
    storedConvertedNumsWithPluses.append(str(convertedNum))
    storedConvertedNumsWithPluses.append("+")

#need to have while until int div = 0 AKA when convertedNumIntPart = 0 

def calculateDecimalToNumberSystem(numInPlaceVal : int, numberToDivBy : int):
    convertedNumIntPart = numInPlaceVal//numberToDivBy
    convertedNumRemPart = numInPlaceVal % numberToDivBy
    print(f'{numInPlaceVal} // {numberToDivBy} = {convertedNumIntPart}')
    print(f'{numInPlaceVal} % {numberToDivBy} = {convertedNumRemPart}')
    storedConvertedNums.append(convertedNumRemPart)

    return convertedNumIntPart;


# def printingOfResultsIntToNumSys():
#     print(reversed(storedConvertedNums))

def printingOfResultsNumSysToInt():
    storedConvertedNumsWithPluses.pop()
    print(storedConvertedNumsWithPluses)
    print(f"= {finalNumSysToInt}")

typeOfConversion = input("Would you like to convert from decimal to a number system(1) or from a number system to decimal(2)? :  ")
if typeOfConversion == "1":
    decimal = int(input("What decimal would you like to convert? : "))
    numberSystem = int(input("Please type your number system's base amount of unique numbers (2-9) or 16? : "))
    



    convertedNumIntPart = decimal

    while convertedNumIntPart > 0:
        convertedNumIntPart = calculateDecimalToNumberSystem(convertedNumIntPart, numberSystem)
        print(storedConvertedNums)
        

    print(storedConvertedNums)
    print(f"Final resulting number is: {reversed(storedConvertedNums)}")


    # if numberSystem == "2":
    #     while convertedNumIntPart > 0:
    #         calculateNumberSystemToDecimal()

    # elif numberSystem == "3":
    #     print()
    # elif numberSystem == "4":
    #     print()
    # elif numberSystem == "5":
    #     print()
    # elif numberSystem == "6":
    #     print()
    # elif numberSystem == "7":
    #     print()
    # elif numberSystem == "8":
    #     print()
    # elif numberSystem == "9":
    #     print()
    # elif numberSystem == "16":
    #     print();


elif typeOfConversion == "2":

   


    numberSystem = int(input("Please type your number system's base amount of unique numbers (1-9) or 16? : ").lower())



    if numberSystem == 16:
        numberInSystem = input("What Hexadecimal wounld you like to convert? : ").lower()
    elif numberSystem <= 9 or numberSystem >= 1:
        numberInSystem = int(input("What number in your number system would you like to convert from? : "))

    # BINARY
    if numberSystem == 2:

        while str(numberInSystem).find("2")>-1 or str(numberInSystem).find("3")>-1 or str(numberInSystem).find("4")>-1 or str(numberInSystem).find("5")>-1 or str(numberInSystem).find("6")>-1 or str(numberInSystem).find("7")>-1 or str(numberInSystem).find("8")>-1 or str(numberInSystem).find("9")>-1  :
            print("A binary number only has ones and zeros")
            numberInSystem = int(input("Please type a number only with ones and zeros: "))
        numberInSystem = [int(x) for x in str(numberInSystem)]
        count = 0
        for i in reversed(numberInSystem):
            calculateNumberSystemToDecimal(i,2,count)
            count+=1
        for i in storedConvertedNums:
            finalNumSysToInt += i
        printingOfResultsNumSysToInt()

    # TERNARY
    elif numberSystem == 3:
        count = 0
        
        while str(numberInSystem).find("3")>-1 or str(numberInSystem).find("4")>-1 or str(numberInSystem).find("5")>-1 or str(numberInSystem).find("6")>-1 or str(numberInSystem).find("7")>-1 or str(numberInSystem).find("8")>-1 or str(numberInSystem).find("9")>-1  :
            print("A ternary number only contains numbers within 0-2")
            numberInSystem = int(input("Please type a number only with 0-2s: "))
        numberInSystem = [int(x) for x in str(numberInSystem)]
        for i in reversed(numberInSystem):
            calculateNumberSystemToDecimal(i,3,count)
            count += 1
        for i in storedConvertedNums:
            finalNumSysToInt += i
        printingOfResultsNumSysToInt()
# 10202
    # QUARTERNARY
    elif numberSystem == 4:
        while str(numberInSystem).find("4")>-1 or str(numberInSystem).find("5")>-1 or str(numberInSystem).find("6")>-1 or str(numberInSystem).find("7")>-1 or str(numberInSystem).find("8")>-1 or str(numberInSystem).find("9")>-1  :
            print("A quarternary number only contains numbers within 0-3")
            numberInSystem = int(input("Please type a number only with 0-3s: "))
        numberInSystem = [int(x) for x in str(numberInSystem)]
        count = 0
        for i in reversed(numberInSystem):
            calculateNumberSystemToDecimal(i,4,count)
            count += 1
        for i in storedConvertedNums:
            finalNumSysToInt += i
        printingOfResultsNumSysToInt()

    #  QUINARY
    elif numberSystem == 5:
        while str(numberInSystem).find("5")>-1 or str(numberInSystem).find("6")>-1 or str(numberInSystem).find("7")>-1 or str(numberInSystem).find("8")>-1 or str(numberInSystem).find("9")>-1  :
            print("A quinary number only contains numbers within 0-4")
            numberInSystem = int(input("Please type a number only with 0-4s: "))
        numberInSystem = [int(x) for x in str(numberInSystem)]
        count = 0
        for i in reversed(numberInSystem):
            calculateNumberSystemToDecimal(i,5,count)
            count += 1
        for i in storedConvertedNums:
            finalNumSysToInt += i
        printingOfResultsNumSysToInt()

    # SENARY
    elif numberSystem == 6:
        while str(numberInSystem).find("6")>-1 or str(numberInSystem).find("7")>-1 or str(numberInSystem).find("8")>-1 or str(numberInSystem).find("9")>-1  :
            print("A senary number only contains numbers within 0-5")
            numberInSystem = int(input("Please type a number only with 0-5s: "))
        numberInSystem = [int(x) for x in str(numberInSystem)]
        count = 0
        for i in reversed(numberInSystem):
            calculateNumberSystemToDecimal(i,6,count)
            count += 1
        for i in storedConvertedNums:
            finalNumSysToInt += i
        printingOfResultsNumSysToInt()

    # SEPTINARY
    elif numberSystem == 7:
        while str(numberInSystem).find("7")>-1 or str(numberInSystem).find("8")>-1 or str(numberInSystem).find("9")>-1  :
            print("A senary number only contains numbers within 0-6")
            numberInSystem = int(input("Please type a number only with 0-6s: "))
        numberInSystem = [int(x) for x in str(numberInSystem)]
        count = 0
        for i in reversed(numberInSystem):
            calculateNumberSystemToDecimal(i,7,count)
            count += 1
        for i in storedConvertedNums:
            finalNumSysToInt += i
        printingOfResultsNumSysToInt()

    # OCTAL
    elif numberSystem == 8:
        while  str(numberInSystem).find("8")>-1 or str(numberInSystem).find("9")>-1  :
            print("An octal number only contains numbers within 0-7")
            numberInSystem = int(input("Please type a number only with 0-7s: "))
        numberInSystem = [int(x) for x in str(numberInSystem)]
        count = 0
        for i in reversed(numberInSystem):
            calculateNumberSystemToDecimal(i,8,count)
            count += 1
        for i in storedConvertedNums:
            finalNumSysToInt += i
        printingOfResultsNumSysToInt()

    # NONAL
    elif numberSystem == 9:
        while  str(numberInSystem).find("9")>-1  :
            print("An octal number only contains numbers within 0-8")
            numberInSystem = int(input("Please type a number only with 0-8s: "))
        numberInSystem = [int(x) for x in str(numberInSystem)]
        count = 0
        for i in reversed(numberInSystem):
            calculateNumberSystemToDecimal(i,9,count)
            count += 1
        for i in storedConvertedNums:
            finalNumSysToInt += i
        printingOfResultsNumSysToInt()

    # HEXADECiMAIL
    elif numberSystem == 16:
        while  not( numberInSystem.find("0")>-1 or numberInSystem.find("1")>-1 or numberInSystem.find("2")>-1 or numberInSystem.find("3")>-1 or numberInSystem.find("4")>-1 or numberInSystem.find("5")>-1 or numberInSystem.find("6")>-1 or numberInSystem.find("7")>-1 or numberInSystem.find("8")>-1 or numberInSystem.find("9")>-1  )      or       not(numberInSystem.find("a")>-1 or numberInSystem.find("b")>-1 or numberInSystem.find("c")>-1 or numberInSystem.find("e") or numberInSystem.find("f") ):
            print("A hexadecimal number only contains numbers within 0-9 and A-F")
            numberInSystem = input("Please type a number only with 0-9s and A-F's: ").lower()
        count = 0
        numberInSystem = [str(x) for x in str(numberInSystem)]
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
            else:
                calculateNumberSystemToDecimal(int(i),16,count)
            count += 1
        for i in storedConvertedNums:
            finalNumSysToInt += i
        printingOfResultsNumSysToInt()
    else:
        print(f"{numberSystem} number system dose not exist or is not a convertable option.")
        numberSystem = input("Try another number system to convert from: ").lower()
else: 
    print("That conversion is not an option. OR you may have mistyped.")
    print("Try again.")
    typeOfConversion = input("Would you like to convert from hexadecimal to a number system or from a number system to hexadecimal? :  ")


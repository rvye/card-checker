def getCardNumber():
    cardnum = int(input("Card Number: "))

    # Puts the card number into an array
    cardnum = [int(x) for x in str(cardnum)]
    
    # VISA16 & MASTERCARD Checker
    if len(cardnum) == 16:
        # Splitting the numbers up (1, 3, etc) and (2, 4, etc)
        cardnumarray = [cardnum[1], cardnum[3], cardnum[5], cardnum[7], cardnum[9], cardnum[11], cardnum[13], cardnum[15]]
        cardmultipliedarray = [int(cardnum[0])*2, int(cardnum[2]*2), int(cardnum[4])*2, int(cardnum[6])*2, int(cardnum[8])*2, int(cardnum[10])*2, int(cardnum[12])*2, int(cardnum[14])*2]        
            
    # VISA13 Checker.
    elif len(cardnum) == 13:
        cardnumarray = [cardnum[1], cardnum[3], cardnum[5], cardnum[7], cardnum[9], cardnum[11]]
        cardmultipliedarray = [int(cardnum[0])*2, int(cardnum[2])*2, int(cardnum[4])*2, int(cardnum[6])*2, int(cardnum[8])*2, int(cardnum[10])*2, int(cardnum[12])*2]
            
    # AMEX Checker
    elif len(cardnum) == 15:
        cardnumarray = [cardnum[0], cardnum[2], cardnum[4], cardnum[6], cardnum[8], cardnum[10], cardnum[12], cardnum[14]]
        cardmultipliedarray = [int(cardnum[1])*2, int(cardnum[3])*2, int(cardnum[5])*2, int(cardnum[7])*2, int(cardnum[9])*2, int(cardnum[11])*2, int(cardnum[13])*2]


    # Getting the individual digits from cardmultipliedarray
    cardmultiplieddigits = []
    for i in range(len(cardmultipliedarray)):
        cardmultiplieddigits += str(cardmultipliedarray[i])

    cardmultiplied = 0
    for i in range(len(cardmultiplieddigits)):
        cardmultiplied += int(cardmultiplieddigits[i])

    # Getting the numbers from cardnumarray & adding cardmultipled with cardnum
    cardnumadded = 0
    for i in range(len(cardmultipliedarray)):
        cardnumadded += int(cardnumarray[i])    
    cardnumadded = cardnumadded + cardmultiplied

    print(cardnumarray)        
    print(cardnumadded)
    print(cardnum)
    print(cardmultiplied)
    print(cardmultiplieddigits)
    print(cardmultipliedarray)
        
    # Checking if the second digit of cardnumadded is a 0
    if [int(x) for x in str(cardnumadded)][1] != 0 or len(str(cardnumadded)) == 2 or 4 or 6:
        print("INVALID.")

        return False

    # Checking if it's a VISA, AMEX, or MASTERCARD
    if cardnum[0] == 4:
        print("VISA")
            
        return True
    elif cardnum[0] == 3 and cardnum[1] == 4 or 7:
        print("AMEX")
            
        return True
    elif cardnum[0] == 5 and cardnum[1] == 1 or 2 or 3 or 4 or 5:
        print("MASTERCARD")
            
        return True

# error handling
try:
    getCardNumber()
except UnboundLocalError and ValueError:
    print("INVALID.")

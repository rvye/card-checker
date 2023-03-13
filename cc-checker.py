def getCardNumber():
    # cardnum = int(input("Card Number: "))

    # cardnum =  4003600000000014

    

    # Puts the card number into an array
    cardnum = [int(x) for x in str(cardnum)]


    if len(cardnum) == 16:


        # Splitting the numbers up (1, 3, etc) and (2, 4, etc)
        cardnumarray = [{cardnum[1]}, {cardnum[3]}, {cardnum[5]}, {cardnum[7]}, {cardnum[9]}, {cardnum[11]}, {cardnum[13]}, {cardnum[15]}]
        cardmultipliedarray = [{int(cardnum[0])*2}, {int(cardnum[2]*2)}, {int(cardnum[4])*2}, {int(cardnum[6])*2}, {int(cardnum[8])*2}, {int(cardnum[10])*2}, {int(cardnum[12])*2}, {int(cardnum[14])*2}]

        # Getting the individual digits from cardmultipliedarray
        cardmultiplieddigits = []
        for i in range(8):
            cardmultiplieddigits += str(cardmultipliedarray[i]).replace('{', '').replace('}','')

        cardmultiplied = 0
        for i in range(9):
            cardmultiplied += int(str(cardmultiplieddigits[i]).replace('{','').replace('}',''))

        # Getting the numbers from cardnumarray & adding cardmultiplied with cardnum
        cardnumadded = 0
        for i in range(8):
            cardnumadded += int(str(cardnumarray[i]).replace('{','').replace('}',''))
        cardnumadded = cardnumadded + cardmultiplied

        # Checking if the second digit of cardnumadded is a 0.
        if [int(x) for x in str(cardnumadded)][1] != 0 or len(str(cardnumadded)) != 2:
            print("INVALID.")

            return False

        # Checking whether the card is a Visa, or MasterCard
        if cardnum[0] == 4:
            print("VISA")
        elif cardnum[0] == 5 and cardnum[1] == 1 or 2 or 3 or 4 or 5:
            print("MASTERCARD")
    if len(cardnum) == 13:
        cardnumarray = [{cardnum[1]}, {cardnum[3]}, {cardnum[5]}, {cardnum[7]}, {cardnum[9]}, {cardnum[11]}, {cardnum[13]}]
        cardmultipliedarray = [{int(cardnum[0])*2}, {int(cardnum[2])*2}, {int(cardnum[4])*2}, {int(cardnum[6])*2}, {int(cardnum[8])*2}, {int(cardnum[10])*2}, {int(cardnum[12])*2}]

        # Getting the individual digits from cardmultipliedarray
        cardmultiplieddigits = []
        for i in range(8):
            cardmultiplieddigits += str(cardmultipliedarray[i]).replace('{','').replace('}','')

        cardmultiplied = 0
        for i in range(9):
            cardmultiplied += int(str(cardmultiplieddigits[i]).replace('{','').replace('}',''))

        # Getting the numbers from cardnumarray & adding cardmultipled with cardnum
        cardnumadded = 0
        for i in range(8):
            cardnumadded += int(str(cardnumarray[i]).replace('{','').replace('}',''))
        cardnumadded = cardnum + cardmultiplied

        # Checking if the second digit of cardnumadded is a 0
        if [int(x) for x in str(cardnumadded)][0] != 0 or len(str(cardnumadded)) != 2:
            print("INVALID.")

            return False

        if cardarray[0] == 4:
            print("VISA")
getCardNumber()

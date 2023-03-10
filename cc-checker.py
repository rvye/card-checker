def getCardNumber():
    cardnum = int(input("Card Number: "))
    
    # Puts the card number into an array
    cardnum = [int(x) for x in str(cardnum)]

    # Splitting the numbers up (1, 3, etc) and (2, 4, etc)
    cardnumarray = [{cardnum[0]}, {cardnum[2]}, {cardnum[4]}, {cardnum[6]}, {cardnum[8]}, {cardnum[10]}, {cardnum[12]}, {cardnum[14]}]
    cardmultipliedarray = [{int(cardnum[1])*2}, {int(cardnum[3])*2}, {int(cardnum[5])*2}, {int(cardnum[7])*2}, {int(cardnum[9])*2}, {int(cardnum[11])*2}, {int(cardnum[13])*2}, {int(cardnum[15])*2}]


    print(cardnumarray)
    print(cardmultipliedarray)
    carda = 0
    cardb = 0
    cardc = 0
    # Adds {cardnumarray} and {cardmultipliedarray}
    for i in range(8):
        """
        Converts each number in the arrays to strings,
        allowing for .replace() to remove the {},
        then converted to integers to add to carda,
        aswell as cardb, then adding carda and cardb together.
        """
        carda += int(str(cardnumarray[i]).replace('{','').replace('}',''))
        cardb += int(str(cardmultipliedarray[i]).replace('{','').replace('}',''))
        print(f"A - Iteration {i}: {carda}")
        print(f"B - Iteration {i}: {cardb}")
        
    cardc = carda + cardb
    print(cardc)
    # Checking if the end digit of cardc is a zero
    cardc = [int(x) for x in str(cardc)]; 
    if cardc[1] != 0:
        print("Invalid")
    
    
getCardNumber()

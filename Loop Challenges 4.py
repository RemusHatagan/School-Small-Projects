loop = True
count = 0
while loop == True:
    name = input("Name someone you want to invite to the party ")
    count = count + 1
    redo = input("Do you want to invite someone else? y/n ").upper()
    if redo == "Y":
        loop = True
    if redo == "N":
        print("You have invited ",count," people.")

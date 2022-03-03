import sys
firstLoop = True
while firstLoop == True:
    print("Welcome to the start of the code")
    secondLoop = True
    OneTwoOrThree = int(input("For the second loop, enter a 1 or 2 or 0 to fully exit >>> "))
    while secondLoop == True:

        if OneTwoOrThree == 0:
            print("You entered a zero")
            print("Exiting")
            secondLoop = False
            exit(sys)
        elif OneTwoOrThree == 1:
            print("You entered a one")
        elif OneTwoOrThree == 2:
            print("You entered a two")

        exitSecondLoop = int(input("Enter a 1 or 2 or 0 to exit second loop >>> "))
        if exitSecondLoop == 0:
            print("You enterd a zero")
            print("Starting again...")
            print("")
            secondLoop = False
            
        if exitSecondLoop == 1:
            print("You enterd a one")
            print("")
        
        if exitSecondLoop == 2:
            print("You enterd a two")
            print("")

            

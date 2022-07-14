
def big():
    print("")
    print("Think Big.")
    print("")

def bigger():
    print("")
    print("Think Bigger.")
    print("")

def winning():
    print("")
    print("Winning.")
    print("")

def winner():
    print("")
    print("Winner.")
    print("")

def userExit():
    print("")
    print("Bye.")
    print("")

def menu():
    print("")
    print("Welcome to Mr Spero's new game.")
    print("")
    print("Press 1 to Think Big >> ")
    print("Press 2 to Think Bigger >> ")
    print("Press 3 for Winning >> ")
    print("Press 4 for Winner >> ")
    print("Press 5 to exit >> ")
    print("")

    userInput = int(input("Enter 1, 2, 3, 4 or 5 >> "))
    
    if userInput == 1:
        big()
    elif userInput == 2:
        bigger()
    elif userInput == 3:
        winning()
    elif userInput == 4:
        winner()
    elif userInput == 5:
        userExit()
    else:
        print("")
        print("Invalid input. Please try again. ")
        menu()
        
menu()

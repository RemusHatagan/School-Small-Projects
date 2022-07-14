
def CreativeMode():
    print("")
    print("Creative chosen .")
    print("")

def SurvivalMode():
    print("")
    print("Survival chosen .")
    print("")

def HardcoreMode():
    print("")
    print("Hardcore chosen .")
    print("")

def AdventureMode():
    print("")
    print("Adventure chosen .")
    print("")

def userExit():
    print("")
    print("Exiting ...")
    print("")

def menu():
    print("")
    print("Welcome to the Minecraft Main Menu.")
    print("")
    print("Press 1 for Creative >> ")
    print("Press 2 for Survival >> ")
    print("Press 3 for Hardcore >> ")
    print("Press 4 for Adventure >> ")
    print("Press 5 to exit >> ")
    print("")

    userInput = int(input("Enter 1, 2, 3, 4 or 5 >> "))
    
    if userInput == 1:
        CreativeMode()
    elif userInput == 2:
        SurvivalMode()
    elif userInput == 3:
        HardcoreMode()
    elif userInput == 4:
        AdventureMode()
    elif userInput == 5:
        userExit()
    else:
        print("")
        print("Invalid input. Please try again. ")
        menu()
        
menu()

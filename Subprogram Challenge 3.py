
def player1Game():
    print("")
    print("1 player games chosen .")
    print("")

def player2Game():
    print("")
    print("2 players games chosen .")
    print("")

def OnlineGame():
    print("")
    print("Online player games chosen .")
    print("")

def userExit():
    print("")
    print("Exiting ...")
    print("")

def menu():
    print("")
    print("Welcome.")
    print("")
    print("Press 1 for 1 player games >> ")
    print("Press 2 for 2 player games >> ")
    print("Press 3 for online player games >> ")
    print("Press 4 to exit >> ")
    print("")

    userInput = int(input("Enter 1, 2, 3 or 4 >> "))
    
    if userInput == 1:
        player1Game()
    elif userInput == 2:
        player2Game()
    elif userInput == 3:
        OnlineGame()
    elif userInput == 4:
        userExit()
    else:
        print("")
        print("Invalid input. Please try again. ")
        menu()
        
menu()

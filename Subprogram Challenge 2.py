
def Domination():
    print("")
    print("Welcome to the Domination Lobby.")
    print("")
def teamDeathmatch():
    print("")
    print("Welcome to the Team Deathmatch Lobby.")
    print("")
def Headquarters():
    print("")
    print("Welcome to the Headquarters Lobby.")
    print("")

def menu():
    print("")
    print("Press (1) for Domination ")
    print("Press (2) for Team Deathmach ")
    print("Press (3) for Headquarters ")
    print("")
    
    userInput = int(input("Please enter your option >>> "))

    if userInput == 1:
        Domination()
    elif userInput == 2:
        teamDeathmatch()
    elif userInput == 3:
        Headquarters()

menu()

    

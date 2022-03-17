direction = str(input("Do you want to count up or down? (U/D) >>> ")).lower()
if direction == "u":
    topNumber = int(input("Enter the top number please >>> "))
    for i in range(1,topNumber+1):
        print(i)
elif direction == "d":
    firstNumber = int(input("Enter a number below 20 please >>> "))
    for i in range(20,firstNumber):
        print(i)
else:
    direction != "d" or direction != "u"
    print("I dont understand!")

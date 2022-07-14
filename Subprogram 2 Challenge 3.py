
def takeInput():
    num = int(input("Enter a number above two >>> "))
    return num

number = takeInput()
number = number + 1

def counting(number):
    for i in range(2, number):
        print(i)

counting(number)

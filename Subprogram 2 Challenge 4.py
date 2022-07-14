
import random

def inputTake():
    num1 = int(input("Enter a small number >>> "))
    num2 = int(input("Enter a big number >>>"))
    comp_num = random.randint(num1, num2)
    return(comp_num)

def guess():
    print("I am thinking of a number... ")
    guessNum = int(input("Enter the number I am thinking of >>> "))
    return guessNum

y = inputTake()

def checker():
    x = guess()
    while x != y:
        print("Wrong! Guess again.")
        x = guess()
    if x == y:
        print("Correct! You win!")

checker()

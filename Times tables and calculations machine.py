
#times tables

def timestables():
  times_table=int(input("Which times table do you wish to see? (2-12) >>>"))
  
  if times_table > 12:
    print("Sorry, we don't have that times table yet.")
    
  if times_table == 1:
      for loopCounter2 in range(13):
            print("1 x",loopCounter2,"=",1*loopCounter2)
  elif times_table == 2:
      for loopCounter2 in range(13):
            print("2 x",loopCounter2,"=",2*loopCounter2)
  elif times_table == 3:
    for loopCounter2 in range(13):
            print("3 x",loopCounter2,"=",3*loopCounter2)
  elif times_table == 4:
    for loopCounter2 in range(13):
            print("4 x",loopCounter2,"=",4*loopCounter2)
  elif times_table == 5:
    for loopCounter2 in range(13):
            print("5 x",loopCounter2,"=",5*loopCounter2)
  elif times_table == 6:
    for loopCounter2 in range(13):
            print("6 x",loopCounter2,"=",6*loopCounter2)
  elif times_table == 7:
    for loopCounter2 in range(13):
            print("7 x",loopCounter2,"=",7*loopCounter2)
  elif times_table == 8:
    for loopCounter2 in range(13):
            print("8 x",loopCounter2,"=",8*loopCounter2)
  elif times_table == 9:
    for loopCounter2 in range(13):
            print("9 x",loopCounter2,"=",9*loopCounter2)
  elif times_table == 10:
    for loopCounter2 in range(13):
            print("10 x",loopCounter2,"=",10*loopCounter2)
  elif times_table == 11:
    for loopCounter2 in range(13):
            print("11 x",loopCounter2,"=",11*loopCounter2)
  elif times_table == 12:
    for loopCounter2 in range(13):
            print("12 x",loopCounter2,"=",12*loopCounter2)
  
      
  repeat = input("Do you wish to see another times table? (Y/N) >>>")
  if repeat == "Y":
    timestables()
  if repeat == "N":
    start()
    
#multiplication

def multiply(number1,number2):
    product = number1*number2
    print("Your product is",product)
    repeat = input("Do you wish to do another calculation? (Y/N) >>>")
    if repeat == "Y":
        calculations()
    if repeat == "N":
        start()
      
#division
    
def divide(number1,number2):
    quotient = number1/number2
    print("Your quotient is",quotient)
    repeat = input("Do you wish to do another calculation? (Y/N) >>>")
    if repeat == "Y":
        calculations()
    if repeat == "N":
       start()

#adding
    
def add(number1,number2):
    total =number1+number2
    print("Your total is",total)
    repeat = input("Do you wish to do another calculation? (Y/N) >>>")
    if repeat == "Y":
        calculations()
    if repeat == "N":
       start()

#subtraction
    
def subtract(number1,number2):
    difference = number1-number2
    print("Your difference is",difference)
    repeat = input("Do you wish to do another calculation? (Y/N) >>>")
    if repeat == "Y":
        calculations()
    if repeat == "N":
       start()

#start

def start():
    start = str(input("Do you wish to do maths? (Y/N) >>> "))
    if start == "Y":
        selection()
    if start == "N":
        exit
        
#selection

def selection():
    selection = str(input("Do you wish to see the times tables (1) or do calculations? (2) >>> "))
    if selection == "1":
             timestables()
    if selection == "2":
             calculations()
         
#calculations
    
def calculations():
    calculation=str(input("Do you want to divide, multiply, add or subtract? "))
    number1=float(input("Enter a number >>> "))
    number2=float(input("Enter another number >>> "))

#choosing calculation
    
    if calculation == "divide":
        divide(number1,number2)

    if calculation == "multiply":
        multiply(number1,number2)

    if calculation == "add":
        add(number1,number2)

    if calculation == "subtract":
        subtract(number1,number2)

print("\u0332".join("Welcome to the times tables and calculations machine!"))
print("")

start()

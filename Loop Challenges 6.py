number = int(input("Please enter a number between 10 and 20 >>>"))
while number < 10:
   print("Too low.")
   number = int(input("Please enter a number between 10 and 20 >>>"))
while number > 20:
   print("Too high.")
   number = int(input("Please enter a number between 10 and 20 >>>"))
if 10 < number < 20: 
  print("Thank you!")

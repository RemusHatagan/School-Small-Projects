compnum = 50
number = int(input(" Enter a number >>> "))
count = 1
while number != compnum:
    if number > compnum:
        print("Too high!")
        count = count + 1
    elif number < compnum:
        print("Too low!")
        count = count + 1
    number = int(input(" Enter a number >>> "))
if number == compnum:
    print("Well done, you took",count,"attempts.")

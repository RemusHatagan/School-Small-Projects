rhyme = input("Enter the first line of a nuresry rhyme >>> ")
length = len(rhyme)
print("This has ",length,"letters in it.")
startingNum = int(input("Enter a starting number >>> "))
endingNum = int(input("Enter a ending number >>> "))
section = rhyme[startingNum : endingNum]
print(section)

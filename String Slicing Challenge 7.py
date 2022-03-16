first_name = input("Enter your first name >>> ")
first = first_name[0]
length = len(first_name)
rest = first_name[1:length]
if first != "a" and first != "e" and first != "i" and first != "o" and first != "u":
    newword = rest + first + "ay"
else:
    newword = first_name + "way"
print(newword.lower())

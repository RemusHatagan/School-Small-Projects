file = open("names.txt", "a")
name = str(input("Enter a name >>> "))
name = name + "\n"
file.write(name)
file.close()
read = open("names.txt", "r")
for line in read.readlines():
    print(line)
file.close()

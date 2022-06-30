def main():
    data = open("personData.txt" , "a")
    firstName = str(input("Enter your first name >>> "))
    lastName = str(input("Enter your last name >>> "))
    age = str(input("Enter your age >>> "))
    data.write("\n"+firstName)
    data.write(lastName +"\n")
    data.write(age +"\n")
    choice = str(input("Do you want to add another user? (Y/N) >>> ")).upper()
    if choice == "Y":
        main()
    else:
        exit()

main()

file.close()
as

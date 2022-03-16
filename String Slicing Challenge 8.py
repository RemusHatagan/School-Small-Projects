def main():
    sentry = True
    while sentry == True:
        first_name = input("Enter your first name >>> ")
        membership = first_name[0:3]+"1"
        print(membership)
main()

first_name = input("Enter your first name >>> ")
if len(first_name) < 5:
    last_name = input("Enter your last name as well >>> ")
    name = first_name + last_name
    print(first_name.upper())
else:
    print(first_name.lower())

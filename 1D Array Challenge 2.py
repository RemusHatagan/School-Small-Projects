cars = []
sentry = True
while sentry == True:
    newCar = str(input("Input a car brand or press x to exit >>> ")).lower()
    if newCar == "x":
        print("Exiting...")
        print("The cars in the list are > ",cars)
        sentry = False
    else:
        cars.append(newCar)

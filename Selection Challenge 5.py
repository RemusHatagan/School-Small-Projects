rain = str(input("Is it raining? (YES/NO) >>>"))
lowRain = rain.lower()

if rain == "YES":
    wind = str(input("Is it windy? (YES/NO) >>>"))
    if wind == "YES":  
        print("It is too windy for an umbrella")
    else:
        print("Take an umbrella")

    
else:
    print("Enjoy your day!")

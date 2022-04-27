food = []
for i in range(4):
    newFood = str(input("Enter another food >>> "))
    food.append(newFood)
print(food)
location = int(input("Which food do you want to delete 1-4 ? >>> "))
location = location - 1
del food[location]
print(food)

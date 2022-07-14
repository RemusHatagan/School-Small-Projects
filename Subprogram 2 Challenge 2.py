
PI = 3.14

def circleArea(PI, radius):
    area = PI * radius * radius
    return area

def circleCirc(PI, radius):
    circum = PI * 2 * radius
    return circum

radius = float(input("Enter the radius of the circle >>> "))

circleArea(PI, radius)
circleCirc(PI, radius)

area = circleArea(PI, radius)
circumference = circleCirc(PI, radius)

print("Area = ",area,"cm ,","Circumference =",circumference,"cm")

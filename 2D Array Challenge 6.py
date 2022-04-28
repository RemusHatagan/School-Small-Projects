range1 = int(input("Enter the number of columns >>> "))
range2 = int(input("Enter the number of rows >>> "))

EmptyArray = [
    [0 for column in range(range1)]
    for row in range(range2)]
print(EmptyArray)

rowChange = int(input("What row index? >>> ")) - 1
columnChange = int(input("What column index? >>> ")) - 1
valueChange = int(input("What integer? >>> "))

print(valueChange)
print(EmptyArray[0][1])

EmptyArray[rowChange][columnChange] = valueChange
print(EmptyArray)

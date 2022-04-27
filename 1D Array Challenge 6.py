nums = []
number = int(input("Enter a number >>> "))
nums.append(number)
while len(nums) < 3:
    number = int(input("Enter a number >>> "))
    nums.append(number)

sentry = True
while sentry == True:
    choice = str(input("Do you want to keep the last number? (Y/N) >>> ")).lower()
    if choice == "y":
        print(nums)
        sentry = False
    if choice == "n":
        del nums[2]
        print(nums)
        sentry = False
        

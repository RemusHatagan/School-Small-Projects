TV_Titles = ["Spiderman","Superman","Venom","The Incredibles"]
for i in TV_Titles:
    print(i)
newShow = str(input("Enter another TV show >>> "))
position = int(input("Enter the position at which you want to put it in 1-5 >>> "))
position = position - 1
TV_Titles.insert(position, newShow)
print(TV_Titles)

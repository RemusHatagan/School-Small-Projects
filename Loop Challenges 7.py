bottles = 10
while 0 < bottles <= 10 :
  print(bottles,"green bottles hanging on the wall")
  print(bottles,"green bottles hanging on the wall")
  bottles= bottles - 1
  guess =int(input("And if 1 green bottle should accidentally fall. How many green bottles will there be hanging on the wall? "))
  if guess == bottles:
    print(bottles,"green bottles hanging on the wall")
    print(bottles,"green bottles hanging on the wall")
    bottles= bottles - 1
    guess =int(input("And if 1 green bottle should accidentally fall. How many green bottles will there be hanging on the wall? "))
  while guess != bottles:
    print("No, try again!")
    guess =int(input("And if 1 green bottle should accidentally fall. How many green bottles will there be hanging on the wall? "))

if bottles <= 0:
  print("There are no more green bottles hanging on the wall!")

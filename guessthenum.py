import random

num = random.randint(1,100)
myGuess = 0
tries = 0

while num != myGuess :
    myGuess = int(input("Please enter a number and try to find what number the computer picked=  "))
    if myGuess > num : 
      print("You have gone way too far come closer.")
      tries+= 1
    elif myGuess < num:
      print("That one is smaller, choose a bit bigger one please.")
      tries+= 1
    else:
      print("Congrats! Your guess is true. You found ", str(num) ,"in" ,str(tries) ,"tries")            
    
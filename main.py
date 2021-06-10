import random

def dice_roll():
  roll = random.randint(1,6)
  print("Welcome to my dice rolling sim! :D")
  print("Here you will randomly recive a number from 1 to 6")
  print("Like a real dice does!")
  print("Here is your first roll: " + str(roll))
  while True:
    like = input("would you like to roll again? ")
    if like == "yes":
      roll = random.randint(1,6)
      print("Your new dice roll is: " + str(roll))
    elif like == "no":
      print("Okay.")
      print("Your final roll is: " + str(roll))
      print("Bye! :)")
      break
    else:
      print("I don't understand.")
      print("Try again.")

dice_roll()
#Dice Simulator Program
from math import floor
from random import randint
dice_vals = []
yes = True
while(yes):
    sum_of_rolls = 0
    snake_eyes = 0
    trials = int(input("How many die are you rolling? "))
    expected_snake_eyes = trials/36 #1/36 is the probabilty of getting 1 snake eyes
    print("Expected number of snake eyes: ",expected_snake_eyes)
    for x in range(trials):
        rolled_val = randint(1,6)
        sum_of_rolls+=rolled_val
        dice_vals.append(rolled_val)
        if x > 0 and dice_vals[x-1] + dice_vals[x] == 2:
            snake_eyes+=1
    print("You rolled the following value(s): ",dice_vals)
    print("Number of snake eyes: ",snake_eyes)
    print("Average rolled value: ",sum_of_rolls/trials,"\n") #Equals 3.5 as trials increases
    if input("Would you like to go again? y/n: ") == "n":
        yes = False

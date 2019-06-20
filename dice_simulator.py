#Dice Simulator Program
from math import floor
from random import randint
dice_vals = []
dice_num = int(input("How many die are you rolling? "))
expected_snake_eyes = dice_num/36 #1/36 is the probabilty of getting 1 snake eyes
print("Expected number of snake eyes: ",expected_snake_eyes)
snake_eyes = 0
for x in range(dice_num):
    dice_vals.append(randint(1,6))
    #print("You rolled a",dice_vals[x])
    if x > 0 and dice_vals[x-1] + dice_vals[x] == 2:
        snake_eyes+=1
print("Number of snake eyes: ",snake_eyes)

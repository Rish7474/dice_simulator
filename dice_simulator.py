#Dice Simulator Program
from random import randint
dice_vals = []
dice_num = int(input("How many die are you rolling? "))
snake_eyes = 0
for x in range(dice_num):
    dice_vals.append(randint(1,6))
    print("You rolled a",dice_vals[x])
    if x > 0 and dice_vals[x-1] + dice_vals[x] == 2:
        snake_eyes+=1
print(snake_eyes)

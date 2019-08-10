#Dice Simulator Program
from random import randint
import numpy as np
from statistics import mean
trial_points,dice_vals,x,y = [],[],[],[]
yes = True
while(yes):
    sum_of_rolls,snake_eyes = 0,0
    trials = int(input("How many die are you rolling? "))
    expected_snake_eyes = trials/36 #1/36 is the probabilty of getting 1 snake eyes
    print("Expected number of snake eyes: ",expected_snake_eyes)
    for c in range(trials):
        rolled_val = randint(1,6)
        sum_of_rolls+=rolled_val
        dice_vals.append(rolled_val)
        if c > 0 and dice_vals[c-1] + dice_vals[c] == 2:
            snake_eyes+=1
    #print("You rolled the following value(s): ",dice_vals,"\n","Number of snake eyes: ",snake_eyes,"\n")
    print("Number of snake eyes: ",snake_eyes,"\n")
    percent_difference = abs(snake_eyes-expected_snake_eyes)/(snake_eyes+expected_snake_eyes)/2
    trial_points.append([trials,percent_difference])
    if input("Would you like to go again? y/n: ") == "n":
        yes = False
trial_points.sort() #sorts array in order of increasing number of trials
test = []
for c in trial_points:
    x.append(c[0])
for c in trial_points:
    y.append(c[1])
np_x = np.array(x,dtype=np.float64)
np_y = np.array(y,dtype=np.float64)
m = (((mean(np_x)*mean(np_y)) - mean(np_x*np_y)) /((mean(np_x)**2) - mean(np_x**2)))
for c in range(int(input("How many elements do you want to add the test case? "))):
    element = int(input("Enter an element: "))
    ele_perct = element*m
    test.append([ele_perct, element])
test.sort()
print(test[0][1], "is the best suited element to yeild the smallest percent value")

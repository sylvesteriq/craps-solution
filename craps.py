## A Craps Game

## Roll two dices, number from 1 to 6 on a dice
## Calculate the sum on the two upward facing dices


## if sum is 7 or 11 on the first roll you win

## if sum is 2, 3 or 12 on first roll, you lose (i.e house wins)

## if sum is 4,5,6,8,9 or 10 on first roll (sum becomes your point)

## To win you must roll your point again

## If you roll a 7 before rolling your point, you lose


## 
import random


def roll_dice():
    """A function to simulate the rolling of two dice"""
    num_1 = random.randrange(1,7)
    num_2 = random.randrange(1,7)
    print("You rolled a:",num_1, "and a :", num_2)
    sum = num_1 + num_2
    print(sum)
    return sum

game_running = True

while game_running:
    
    dice_roll = roll_dice()
    print(dice_roll)
    
    ## winning condition (If a 7 or 11 is rolled)
    if (dice_roll == 7 or dice_roll == 11):
        print('you win')
        game_running = False
        
    ## losing condition (if a 2, 3 or 12 is rolled)
    elif (dice_roll == 2 or dice_roll == 3 or dice_roll == 12):
        print('You lose: Game Over')
        game_running = False
    
    ## repeating dice roll
    else:
        while game_running:
            first_dice_roll = dice_roll
            next_dice_roll = roll_dice()
            
            if(next_dice_roll == first_dice_roll):
                print('next_dice_roll',next_dice_roll," is equal to ",first_dice_roll,' You win')
                game_running = False
                
            elif(next_dice_roll == 7):
                print('next_dice_roll:',next_dice_roll, ' is equal to 7, so you lose',)
                game_running = False
        
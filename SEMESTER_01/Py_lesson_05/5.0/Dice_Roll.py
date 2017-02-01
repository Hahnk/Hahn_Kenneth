

import random
you =random.randint(1,6)
com =random.randint(1,6)

def rollDice(y,c):
    print ("You rolled a" , y )
    print ("Computer rolled a" , c)
    if y > c :
        print ("You Win!")
    if y <= c :
        print ("you lose...")

rollDice(you,com)

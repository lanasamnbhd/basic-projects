import random

minVal=1
maxVal=6

rollAgain="yes"

while rollAgain=="yes" or rollAgain=="y":
    print("rolling the dices...")
    print("the values are:")

    print(random.randint(minVal,maxVal))
    print(random.randint(minVal, maxVal))

    rollAgain=input("roll the dices again?")
    

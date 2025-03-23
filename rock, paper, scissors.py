import random
choices=["rock","paper","scissors"]
player=False
cpuScore=0
playerScore=0
while True:
    computer=random.choice(choices)
    player=input("rock,paper or scissors?")
    if player==computer:
        print("Draw")
    elif player=="rock":
        if computer=="paper":
            print("you lost!\n",computer+" covers "+player)
            cpuScore+=1
        else:
            print("you win!\n",player+" smashes "+computer)
            playerScore+=1
    elif player=="paper":
        if computer=="scissors":
            print("you lost!\n",computer+" cut "+player)
            cpuScore+=1
        else:
            print("you win!\n",player+" covers "+computer)
            playerScore+=1
    elif player=="scissors":
        if computer=="rock":
            print("you lost!\n",computer+" smashes "+player)
            cpuScore+=1
        else:
            print("you win!\n",player+" cut "+computer)
            playerScore+=1
    elif player=="end":
        print("final score:")
        print(f"COMPUTER: {cpuScore}")
        print(f"PLAYER: {playerScore}")
        break


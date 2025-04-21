name=input("type your name: ")

print("welcome",name, "to this adventure")

answer=input("you are on a dirt road, it has comr to an end and you can go left or right. which way would you like to go? ")
if answer=="left":
    answer=input("you came to a river, you can walk around it or swim accross? type walk to walk around and swim to swim acrross: ")
    
    if answer=="swim":
        print("you swam accros and were eaten by an alligator.")

    elif answer=="walk":
        print("you walked for many miles, ran out of water and dead.")

    else:
        print("not a valid option. you lose. ")



elif answer=="right":
    answer=input("you came to a bridge, it looks wobbly, do you want to cross it or head back? (cross/back):")

    if answer=="back":
        print("you went back and lost the game.")

    elif answer=="cross":
        print("you crossed the bridge and meet a stranger. will you talk to them or not?")

        if answer=="yes":
            print("you talked tothe stranger and they give you gold. you WIN.")

        elif answer=="no":
            print("you ignored the stranger and they are offended and you lose.")

        else:
            print("not a valid option. you lose.")

    else:
        print("not a valid option. you lose. ")



else:
    print("not a valid option. you lose. ")

print("thank you for playing", name)


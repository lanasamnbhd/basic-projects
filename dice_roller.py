import random

one = """
            ("===========")
            ("|         |")
            ("|    O    |")
            ("|         |")
            ("===========")\n
        """

two = """
            ("===========")
            ("|         |")
            ("| O     O |")
            ("|         |")
            ("===========")\n
        """

three = """
            ("===========")
            ("|    O    |")
            ("|    O    |")
            ("|    O    |")
            ("===========")\n
        """

four = """
            ("===========")
            ("| O     O |")
            ("|         |")
            ("| O     O |")
            ("===========")\n
        """

five = """
            ("===========")
            ("| O     O |")
            ("|    O    |")
            ("| O     O |")
            ("===========")\n
        """

six = """
            ("===========")
            ("| O     O |")
            ("| O     O |")
            ("| O     O |")       
            ("===========")\n
        """

outcomesList=[one,two,three,four,five,six]

print("this is a dice roll simulator")
x="y"
while x == "y":
    random_outcome=random.sample(outcomesList,2)
    for outcome in random_outcome:
        print(outcome)

    x=input("press y to roll again")

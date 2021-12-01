import time
import random

def skill_roll(chance):
    roll = random.randint(1,100)
    if roll <=chance:
        degree = (chance - roll)//10
        print("Roll: %d Success with %d degrees" % (roll,degree))
        return 1, roll, degree
    else:
        degree = (roll - chance)//10
        print("Roll: %d Failure with %d degrees" % (roll,degree))
        0, roll, degree

def attack_roll(chance):
    die = random.randint(0,9)
    die10 = random.randint(0, 9)
    roll = (die10*10+die)
    loc = (die*10+die10)
    location = ""
    if loc and loc <16:
        location = "Head"
    elif loc <36:
        location = "Right Arm"
    elif loc <56:
        location = "Left Arm"
    elif loc < 81:
        location = "Body"
    elif loc < 91:
        location = "Right Leg"
    else:
        location = "Left Leg"

    if roll and roll <=chance:
        degree = (chance - roll)//10
        print("Roll: %d Success with %d degrees." % (roll,degree), end=" ")
        print("You hit the: "+location)
        return 1, roll, degree, location
    else:
        degree = (roll - chance)//10
        print("Roll: %d Failure with %d degrees" % (roll,degree))
        return 0, roll, degree, location



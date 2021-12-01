import time
import random

def skill_roll(chance):
    roll = random.randint(1,100)
    if roll <=chance:
        degree = (chance - roll)//10
        print("Roll: %d Success with %d degrees" % (roll,degree))
    else:
        degree = (roll - chance)//10
        print("Roll: %d Failure with %d degrees" % (roll,degree))


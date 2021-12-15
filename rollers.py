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

def magic_roll(power=1, casting_number = 10, bonus=0, winds=0):
    dice = []
    roll = bonus

    #tablica powtórzeń danej liczby
    numbers = [0 for x in range(10)]

    dubs = 0
    trips = 0
    quads = 0
    for i in range(power):
        die = random.randint(1,10)
        dice.append(die)
        numbers[die-1] += 1
        roll += winds
        roll += die

    if numbers[0] == power:
        print("Automatic Failure!")
        return 1, roll, dubs, trips, quads

    for number in numbers:
        if number == 2:
            dubs += 1
        elif number == 3:
            trips += 1
        elif number >= 4:
            quads += 1

    if numbers[0] == power:
        print("Automatic Failure! Dubs: %d, Trips: %d, Quads: %d" % (dubs, trips, quads))
        return 0, roll, dubs, trips, quads

    if roll >= casting_number:
        print("Roll: %d, Success! Dubs: %d, Trips: %d, Quads: %d" % (roll, dubs, trips, quads))
        return 1, roll, dubs, trips, quads
    else:
        print("Roll: %d, Failure! Dubs: %d, Trips: %d, Quads: %d" % (roll, dubs, trips, quads))
        return 0, roll, dubs, trips, quads

def minor_manifestation():
    roll = random.randint(1, 100)
    die = random.randint(1, 10)
    if roll <= 10:
        print("Witchery: Within 10 yards (5 squares) of you, milk curdles, wine goes sour, and food")
    elif roll <= 20:
        print("Rupture: Your nose begins to bleed and continues until you make a successful Toughness Test. You can test once per round. ")
    elif roll <= 30:
        print("Breath of Chaos: A cold and unnatural wind blows through the area.")
    elif roll <= 40:
        print("Horripilation: Your hair stands on end for %d rounds." % (die))
    elif roll <= 50:
        print("Wyrdlight: You glow with an eerie light for %d rounds." % (die))
    elif roll <= 60:
        print("Unnatural Aura: Animals within 10 yards (5 squares) of you get spooked, and unless controlled with an Animal Training Test, flee the scene.")
    elif roll <= 70:
        print("Haunted: Ghostly voices fill the air for the duration of your spell.")
    elif roll <= 80:
        print("Aethyric Shock: The magical energy coursing through you causes you to lose 1 Wound regardless of Toughness Bonus or armour.")
    elif roll <= 90:
        print("Mental Block: You channel too much magical energy. Your Magic Characteristic is reduced by 1 for %d minutes." % (die))
    elif roll <= 95:
        print("Whimsy: The GM can choose any result from this chart or make up a comparable minor effect.")
    elif roll <= 100:
        print("Unlucky!: Roll Major Chaos Manifestation instead.")
        major_manifestation()

def major_manifestation():
    roll = random.randint(1, 100)
    die = random.randint(1, 10)

    if roll <= 10:
        print("itch Eyes: Your pupils turn bright red. They revert to their original colour at dawn the following day.")
    elif roll <= 20:
        print("Silenced: You lose your voice for %d rounds." %(die))
    elif roll <= 30:
        print("Overload: You are overwhelmed by magical energy and are stunned for 1 round.")
    elif roll <= 40:
        print("Craven Familiar: A Daemon Imp (see Chapter 11: Common Creatures and NPCs) appears from the Aethyr and attacks you next round. ")
    elif roll <= 50:
        print("Chaos Foreseen: You get a glimpse of the Realm of Chaos and gain 1 Insanity Point. Any time after this event, you can spend 200 xp and gain the Dark Lore (Chaos) talent.")
    elif roll <= 60:
        print("Aethyric Attack: Magical energy burns through you, causing you to lose %d Wounds regardless of Toughness Bonus or armour." %(die))
    elif roll <= 70:
        print("Enfeeblement: Chaos energy wracks your body, debilitating your constitution. Your Toughness Characteristic is reduced by 10%% for %d minutes." %(die))
    elif roll <= 80:
        print("Mindnumb: You channel too much magical energy. Your Magic Characteristic is reduced by 1 for 24 hours.")
    elif roll <= 90:
        print("Daemonic Possession: You are possessed by a Daemonic entity for one minute. During that time, the GM controls all your actions and when you take control of your body again, you’ll have no memory of what you just did.")
    elif roll <= 95:
        print("Perverse Delight: The GM can choose any result from this chart or make up a comparable major effect.")
    elif roll <= 100:
        print("Trick of Fate: Roll Catastrophic Chaos Manifestation instead.")
        catastrophic_manifestation()

def catastrophic_manifestation():
    roll = random.randint(1, 100)
    die = random.randint(1, 10)

    if roll <= 10:
        print("Wild Magic: You lose control of the magic as you cast your spell. Everyone within 30 yards (15 squares), including you, loses 1 Wound regardless of Toughness Bonus or armour.")
    elif roll <= 20:
        print("The Withering Eye: Chaos energy wracks your body, debilitating your constitution. Your Toughness Characteristic is reduced by 20%% for %d hours" %(die))
    elif roll <= 30:
        print("Tzeentch’s Lash: Magic power overwhelms you, knocking you out for %d minutes." %(die))
    elif roll <= 40:
        print("Aethyric Assault: The Winds of Magic lash out at you. You suffer a Critical Hit to a random location. Critical value: %d" %(die))
    elif roll <= 50:
        print("Heretical Vision: A Daemon Prince shows you a vision of Chaos. You gain %d Insanity Points. Any time after this event, you can spend 100 xp and gain the Dark Lore (Chaos) talent." %(die))
    elif roll <= 60:
        print("Mindeaten: Your ability to use magic is burned out of you. Your Magic Characteristic is reduced to 0. For each full 24 hours that passes, it increases by 1 until it returns to full strength.")
    elif roll <= 70:
        print("Uninvited Company: You are attacked by a number of lesser Daemons equal to your Magic Characteristic (see Chapter 11: Common Creatures and NPCs). They appear from the Aethyr within 12 yards (6 squares) of you.")
    elif roll <= 80:
        print("Daemonic Contract: You suffer %d wounds (regardless of Toughness Bonus and armour) as a two inch Chaos rune \n burns its way onto a random part of your body. Should you ever collect 13 of these, they will spell out a contract that \n signs your soul away to a Ruinous Power (GM’s discretion). Removal of the branded skin will make no difference to the contract." %(die))
    elif roll <= 90:
        print("Called to the Void: You are sucked into the Realm of Chaos and are forever lost. Unless you have a Fate Point to spend, it’s time to roll up a new character. ")
    elif roll <= 100:
        print("Dark Inspiration: The GM can choose any result from this chart or make up a comparable catastrophic effect.")



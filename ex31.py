print("You enter a dark room with two doors. Do you go throught door #1 or door #2?")

door = input(">")

if door == "1":
    print("There 's a giant bear here eating a cheese cake. What do you do? ")
    print("1. Take the cake.")
    print("2. Scream at the bear.")

    bear = input(">")

    if bear == "1":
        print("The bear eats your face off. Good job!")
    elif bear == "2":
        print("The bear eats your legs off. Good job!")
    else:
        print("Well, doing %s is probaly better. Bear run away." %bear)

elif door == "2":
    print("You stare into the endless abyss at Cthulhu 's retina.")
    print("1. Blueberries.")
    print("2. Yellow jacket clothespin.")
    print("3. Understanding revolves Yelling melodies.")

    instanly = input(">")

    if instanly == "1" or instanly == "2":
        print("Your body survives powered by a mind of jello. Good job!")
    else:
        print("The insanity rots your eyes into a pool of muck. Good Job!")

else:
    print("You stumble around and fall on a knife and die. Good job!")

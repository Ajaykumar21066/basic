

#####  BRANCHES AND FUNCTIONS  ######

from sys import exit

def gold_room():
    print " This room is full of gold. How much do u take?"

    choice = raw_input(">> ")
    if "0" in choice or "1" in choice:
        how_much = int(choice)

    else:
        dead("Man, learn to type a number.")


    if how_much < 50:
        print "Nice, you are not greedy , you win!"
        exit(0)

    else:
        dead("You greedy man !")



def bear_room():
    print "There is a bear here"
    print "The bear has a bunch of honey."
    print "the fat bear is in front of the another door."
    print "how aare you going to move the bear."
    bear_moved = False

    while True:
        choice = raw_input(">> ")

        if choice == "take honey":
            dead("The bear looks at you and then slaps your face off.")
        elif choice == "taunt bear" and not bear_moved:
            print "The bear has moved from the door, you can go through it now."
            bear_moved = True
        elif choice == "taunt bear" and bear_moved:
            dead("the bear gets pissed off and chews your leg off.")
        elif choice == "open door" and bear_moved:
            gold_room()

        else:
            print "I got no idea what that means."



def hulu_room():
    print "Here you see the evil Hulu."
    print "He, it, whatever stares at you and you go insane."
    print "Do u flee for you life or eat your head?"


    choice = raw_input(">> ")

    if "flee" in choice:
        start()
    elif "head" in choice:
        dead("well that was tasty!")

    else:
        hulu_room()


def dead(why):
    print why, "Good Job!!!"
    exit(0)


def start():
    print "You are in a dark room."
    print "There is a door to your right and left"
    print "Which one do u take?"


    choice = raw_input(">> ")

    if choice == "left":
        bear_room()
    elif choice == "right":
        hulu_room()

    else:
        dead("You stumble around the room until you starve.")


start()

import time
import pdb
import random
print "teaaaaaaaaaaaaaaaaaast"
##### eelcome to the Dark Cave ########

# game function

def game():
    print ("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print ("Welcome to the cave of secrets!")
    print ("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

    time.sleep(3)


    print "You enter a Dark room out of curiousity, It is dark and you can only see a stick on the floor"
    choice = raw_input("Do you take it >>>, ")


    # STICK TAKEN

    if choice in ['y', 'yes', 'YES', 'Yes', 'yes']:
        print "You have taken the stick"
        time.sleep(2)
        stick = 1

    # STICK not TAKEN

    else:
        print "You did not take the stick"
        stick = 0


    print "As you move in further in the cave, you see a small glowing object"
    choice2 = raw_input("Do you go near the object >>>  ")

    # GO Near the object

    if choice2 in ['y', 'yes', 'YES', 'Yes', 'yes']:
        print "you go near the object"
        time.sleep(2)
        print " As you go closer, you realize that object has a eye"
        time.sleep(2)
        print "The eye belongs to giant spider"
        choice3 = raw_input("Do you try to fight the spider? >>> ")


        #### Fight spider ###
        if choice3 in ['y', 'yes', 'YES', 'Yes', 'yes']:

            # with stick
            if stick == 1:
                print "You only have a stick to fight with"
                print "Jab it quickly in the spoder's eye and get an advantage"
                time.sleep(2)
                print ("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                print ("                  Fighting...                   ")
                print ("   YOU MUST HIT ABOVE A 5 TO KILL THE SPIDER    ")
                print ("IF THE SPIDER HITS HIGHER THAN YOU, YOU WILL DIE")
                print ("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                time.sleep(2)
                your_hit = int(random.randint(3, 10))
                spider_hit = int(random.randint(1, 5))

                print "you hit a %d" % your_hit
                print "spider hits a %d" % spider_hit
                time.sleep(2)

                if spider_hit > your_hit:
                    print " The spider has done more damage tha you"
                    complete = 0
                    return  complete

                elif your_hit < 5:
                    print "You didn't do enough damage, but managed to escape"
                    complete = 1
                    return  complete

                else:
                    print "You killed the spider"
                    complete = 1
                    return  complete


            # Without stick

            else:
                print "You dont have anything to fight with"
                time.sleep(2)

                print ("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                print ("                  Fighting...                   ")
                print ("   YOU MUST HIT ABOVE A 5 TO KILL THE SPIDER    ")
                print ("IF THE SPIDER HITS HIGHER THAN YOU, YOU WILL DIE")
                print ("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                time.sleep(2)
                your_hit = int(random.randint(1, 8))
                spider_hit = int(random.randint(1, 5))
                print "you hit a %d" % your_hit
                print "Spider hits a %d" % spider_hit
                time.sleep(2)

                if spider_hit > your_hit:
                    print " The spider has done more damage tha you"
                    complete = 0
                    return  complete

                elif your_hit < 5:
                    print "You didn't do enough damage, but managed to escape"
                    complete = 1
                    return complete

                else:
                    print "You killed the spider"
                    complete = 1
                    return complete


#### Dont fight the spider

        else:
            print "You choose not to fight the spider "
            time.sleep(1)

            print " As you turn away spider fangs you in the eye"
            complete = 0
            return complete




###### Dont approach spider #####


    else:
        print "You turn way from glowing object and attempt to leave the cave........"
        time.sleep(1)
        print "But something wont let you...."
        time.sleep(2)
        complete = 0
        return complete



### game LOOP


alive = True
while alive:
    print "test11111111111"
    complete = game()
    if complete == 1:
        alive = raw_input("you managed to escape, Would you like to play again? >>>>> ")
        if alive in ['y', 'Y', 'YES', 'yes', 'Yes']:
            alive
        else:
            break

    else:
        alive = raw_input("You have died, Would you like to play again? >>>>> ")
        if alive in ['y', 'Y', 'YES', 'yes', 'Yes']:
            alive
        else:
            break


import random
hp = 100
dec = 0
atk = 5
agi = 0
cha = 0
dex = 0

i = True
while(i):
    start = input("Would you like to start the game?(y/n)")
    if (start == "y"):
        print("You are in a forest, with a pixcaxe, an axe, and a small sword. There is a river nearby, along with the mouth of a small cave.")
        caveRiver = input("do you want to wander by the river or enter the cave? (cave/river)")
    
        if (caveRiver == "cave"):
            print("You look around the cave, but you have no torches to go deeper. You walk back out of the cave.")
            river = input("Would you like to go to the river? (y/n)")
            caveRiver = "river"
        
    if (caveRiver == "river"):
        print("You venture along the river, heading south on the direction of the current. There is a village in the distance.")
        print("You approach the village and are greated by a guard.")
        print("Hello sir, are you here to enter the town of Vilderwork?")
        town = input("Would you like to enter the town? (y/n)")
        
        if (town == "y"):
            print("You enter the town, and are greated with a host of people, all seemingly trying to sell you things.")
            print("Two people stick out to you, one that looks like a shopkeeper of all kinds of swords and armor and another that looks like an old man with a staff.")
            person = input("Which one would you like to aproach? (shop/man)")

            if (person == "man"):
                print("You approach the odd-looking fellow, and as you approach he speaks to you.")
                quest =  input("-Hello there. You look like an adventurer. Would you like to undertake my quest? (y/n)")

                if (quest == "y"):
                    print("Good, good. Here, take these torches so that you can enter. When you came to the village, you may have seen a cave by the river. That cave is EVIL.")
                    print("That cave is EVIL. It must be destroyed, but the way to destroy it is at the bottom of the cave, and there are only reports of what lies there.")
                    cave2 = input("Go to the cave and undetake the quest? (y/n)")

                    if (cave2 == "y"):
                        print("You travel to the cave, and enter with the torches you were given.")
                        print("You travel deeper into the cave and enter a network of long stone tunnels.")
                        print("Suddenly, out of the shadows, comes a skeleton, with 1 ATK, 5 HP and 0 DEF. you have" + hp + "HP," + atk + "ATK, and" + dec + "DEF.")
                        print("The skeleton attacks and you attack back. Skeleton has been destroyed.")
                        fork1 = input("You travel deeper, undettered and fine a fork in the tunnel. Which tunnel would you like to go through? (l/r)")

                        if (fork1 == "r"):
                            print("You travel on the path to your right, and see before you, a chest or pure gold. You open it, and find a leather jacket of +3 defence and +2 agility.")
                            dec += 3
                            agi += 2



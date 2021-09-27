import random # random numbers (https://docs.python.org/3.3/library/random.html)
import sys # system stuff for exiting (https://docs.python.org/3/library/sys.html)

player = {
    "name" : "p1",
    "items" : [],
    "friends" : [],
    "location" : "start"
}

rooms = {
    "room1" : "queens",
    "room2" : "longisland",
    "room3" : "villainhouse"
}

def rollDice(minNum, maxNum, difficulty):
    # any time a chance of something might happen, let's roll a die
    result = random.randint(minNum,maxNum)
    print ("You roll a: " + str(result) + " out of " + str(maxNum))

    if (result <= difficulty):
        print ("trying again....")
        
        input("press enter >")
        rollDice(minNum, maxNum, difficulty) # this is a recursive call

    return result


def printGraphic(name):
    if (name == "title"):
        print ('──────────────▐█████───────')
        print ('──────▄▄████████████▄──────')
        print ('────▄██▀▀────▐███▐████▄────')
        print ('──▄██▀───────███▌▐██─▀██▄──')
        print ('─▐██────────▐███─▐██───██▌─')
        print ('─██▌────────███▌─▐██───▐██─')
        print ('▐██────────▐███──▐██────██▌')
        print ('██▌────────███▌──▐██────▐██')
        print ('██▌───────▐███───▐██────▐██')
        print ('██▌───────███▌──▄─▀█────▐██')
        print ('██▌──────▐████████▄─────▐██')
        print ('██▌──────█████████▀─────▐██')
        print ('▐██─────▐██▌────▀─▄█────██▌')
        print ('─██▌────███─────▄███───▐██─')
        print ('─▐██▄──▐██▌───────────▄██▌─')
        print ('──▀███─███─────────▄▄███▀──')
        print ('──────▐██▌─▀█████████▀▀────')
        print ('──────███──────────────────')
        print ('     "HELP ME, AVENGERS!"     ')

    if (name == "spiderman"):
        print ('────▐──▌─────▐──▌────')
        print ('───▐▌─█───────█─▐▌───')
        print ('──▄█──▀▀▄▌▄▐▄▀▀──█▄──')
        print ('─▐█─▄█▀▄█████▄▀█▄─█▌─')
        print ('──▀▀─▄▄▄█████▄▄▄─▀▀──')
        print ('───▄█▀─▄▀███▀▄─▀█▄───')
        print ('─▄█──▄▀──███──▀▄──█▄─')
        print ('▐█───█───▐█▌───█───█▌')
        print ('─█────█───▀───█────█─')
        print ('─▀█───█───────█───█▀─')
        print ('──█────█─────█────█──')
        print ('───█───█─────█───█───')
        print ('────▌───▌───▐───▐────')
        print ('     "SPIDER MAN"    ')

    if (name == "ironman"):
        print ('░░░░░░░██████████████████░░░░░░░')
        print ('░░░░████▓▓▓█▓▓▓▓▓▓▓▓█▓▓▓███░░░░░')
        print ('░░░██▓▓█▓▓▓█▓▓▓▓▓▓▓▓█▓▓▓█▓▓█░░░░')
        print ('░░██████████▓▓▓▓▓▓▓▓██████████░░')
        print ('░░██──────███████████───────██░░')
        print ('░███───────██▓▓▓▓▓▓█────────███░')
        print ('░████───────█▓▓▓▓▓▓█───────████░')
        print ('░█▓██───────█▓▓▓▓▓▓█───────██▓█░')
        print ('░██▓█───────█▓▓▓▓▓▓█───────█▓██░')
        print ('████▓█──────█▓▓▓▓▓▓█──────█▓████')
        print ('█▓██▓█──────▀██████▀──────█▓██▓█')
        print ('█▓██▓█────────────────────█▓██▓█')
        print ('█▓████────────────────────████▓█')
        print ('█▓██▀──────────────────────▀██▓█')
        print ('█▓██──█▀▀▀▀▄▄──────▄▄▀▀▀▀█──██▓█')
        print ('███───█─────▀██▄▄██▀─────█───███')
        print ('░██───▀█▄▄▄▄█▀────▀█▄▄▄▄█▀───██░')
        print ('░███────────────────────────███░')
        print ('░░█▓█──────────────────────█▓█░░')
        print ('░░█▓▓█────────────────────█▓▓█░░')
        print ('░░█▓▓▓█──────────────────█▓▓▓█░░')
        print ('░░█▓▓▓█──────────────────█▓▓▓█░░')
        print ('░░█▓▓▓▓█▄──────────────▄█▓▓▓▓█░░')
        print ('░░░█▓▓█▀█──▄▀▀▀▀▀▀▀▀▄──█▀█▓▓█░░░')
        print ('░░░░█▓█─▀▄▄▀────────▀▄▄▀─█▓█░░░░')
        print ('░░░░░█▓█─────▄▄▄▄▄▄─────█▓█░░░░░')
        print ('░░░░░░█▓█▄▄▄██▓▓▓▓██▄▄▄█▓█░░░░░░')
        print ('░░░░░░░█▓▓▓█▓▓▓▓▓▓▓▓█▓▓▓█░░░░░░░')
        print ('░░░░░░░░████████████████░░░░░░░░')
        print ('░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░')
        print ('           "IRON MAN"           ')

    if (name == "captainA"):
        print ('─────▄███████████▄─────')
        print ('───████░░░░░░░░░████───')
        print ('─███░░░▄▄█████▄▄░░░███─')
        print ('██░░░██████─██████░░███')
        print ('█░░░██████───██████░░░█')
        print ('█░░███▄▄───────▄▄███░░█')
        print ('█░░██████─────██████░░█')
        print ('█░░█████──▄█▄──█████░░█')
        print ('█░░░███──▄███▄──███░░░█')
        print ('██░░░█████████████░░░██')
        print ('─███░░░▀▀█████▀▀░░░███─')
        print ('───███▄░░░░░░░░░▄███───')
        print ('────▀█████████████▀────')
        print ('   "CAPTAIN AMERICA"   ')

    if (name == "castle"):
        print ('              T~~')
        print ('               |')
        print ('             /"\ ')
        print ('      T~~     |`| T~~')
        print ('  T~~ |    T~ WWWW|')
        print ('  |  /"\   |  |  |/\T~~')
        print (' /"\ WWW  /"\ |1 |WW|')
        print ('WWWWW/\| /   \|1/\|/"|')
        print ('   /__\/]WWW[\/__\WWWW')
        print ('|"  WWWW`|I_I|`WWWW`  |')
        print ('|   |` |/  -  \| |`  |')
        print ('|`  |  |LI=H=LI|` |   |')
        print ('|   |` | |[_]| |  |`  |')
        print ('|   |  |_|###|_|  |   |')
        print ('`---`--`-/___\-`--`---`')


def gameOver():

    #printGraphic("")

    print("-------------------------------")
    print("You are dead...")
    print(player["name"] + "," + "You couldn't save your brother.") 
    print("-------------------GAME OVER-------------------")
    return

def gameWin():

    #printGraphic("")

    print("-------------------------------")
    print ("The villain is DEAD!!")
    print(player["name"] + "," + "You saved your brother!")
    print ("-------------------YOU WIN-------------------") 
    return
    

def introStory():
    # let's introduce them to our world
    player["name"] = input("Please enter your name >")
    print ("...")
    printGraphic("title")
    # intro story, quick and dirty (think star wars style)
    print ("Welcome back to my game, " + player["name"] + "!")
    print ("I heard that a villain took your brother to his castle.")
    print ("and..the villain has very strong power...")
    print ("I think you should find someone to help you.")
    print ("If you want someone to help you, I'll take you somewhere.")
    input("press enter >")
    locQueens()

def locQueens():
    print("You are in Queens now.")
    print("Can you see the school and library?")
    print("Choose where to go out of the two.")
    print("[ school , library ]")

    pcmd = input(">")

    if (pcmd == "school"): 
        print ("You are going to the school...")
        print (". . . ")
        input("press enter >")

        printGraphic("spiderman")
        print ("There is Peter Parker over there!")
        print ("options: [ kidnap him , talk to him ] ")
        pcmd = input(">")

        if (pcmd == "kidnap him"):
            print ("Security guards are coming to catch you.")
            print ("You were kicked out of school.")
            locQueens() #Try again

        elif (pcmd == "talk to him"):
            print (" 'Hey, Spider man. Please help me! Someone took my brother.' ")
            print (" 'Okay, but I can't beat him by myself. We have to find someone else.' ")
            print (" You have two options. Where do you want to go with Spider-man? ")
            player["friends"].append("spiderman")
            print (" [ villain's house, long island, store ]  ")
            pcmd = input(">")

            if (pcmd == "villain's house"):
                print (" You are going to the villain's house . . .")
                print (". . .")
                locVillain()

            elif (pcmd == "long island"):
                print (" You are going to Long island . . . ")
                print (". . .")
                locLongisland()
            
            elif (pcmd == "store"):
                print ("You are going to the store...")
                print (". . . ")
                print (" There is a gun. Do you want to buy it? ")
                print ("> yes , no ")
                pcmd = input(">")

                if (pcmd == "yes"):
                    print ("Now, you have a gun.")
                    player["items"].append("gun")
                    print (" 'Spiderman: Cool. Let's go to Long Island. There will be someone to help us.'  ")
                    pcmd = input(">")
                    print (". . . ")
                    locLongisland()
            
                elif (pcmd == "no"):
                    print (" 'Spiderman: You can't fight without a gun. Buy it!' ")
                    print (" You bought a gun. ")
                    player["items"].append("gun")
                    print (" 'Spiderman: Ok, let's go to Long Island.There will be someone to help us.'  ")
                    pcmd = input(">")
                    print (". . . ")
                    locLongisland()

            else:
                print ( "You can't go there")
                locQueens()

    elif (pcmd == "library"):
        print ("You are going to the library...")
        print (". . . ")
        print (" ----- 'CLOSED' ----- ")
        print (" Oops, the library is closed. You should go back. ")
        pcmd = input("press enter to go back >")
        locQueens()

    


def locLongisland():
    print (" You and Spiderman arrived on Long Island. ")
    print (" There is a Stark tower in front of you. ")
    input(">")
    print (" If you want to enter the tower, you should roll a dice! ")
    input ("Press enter to roll >")

    difficulty = 5
    roll = rollDice(0, 20, difficulty)

    if (roll >= difficulty):
            print ("The door is opened!")
            input(">")
            printGraphic("ironman")
            print ("There is Iron-Man. Do you want to talk to him?")
            print ("[ yes , no ]")
            pcmd = input(">")

            if (pcmd == "yes"):
                print ("Iron-Man: Okay, I can help you. Let' go together!")
                player["friends"].append("ironman")
                input("Press Enter to go to next stage! >")
                locVillain()

            else:
                print ("Then..you can't save your brother. Again, do you want to talk to him?")
                print (" [ yes, no ]")
                pcmd = input(">")
                if (pcmd == "yes"):
                    print ("Iron-Man: Okay, I can help you. Let' go together!")
                    player["friends"].append("ironman")
                    input("Press Enter to go to next stage! >")
                    locVillain()
                
                else:
                    gameOver()


def locVillain():
        printGraphic("castle")
        print ("You arrived at the door of the villain's castle.")
        print ("The villain is coming to you!!")
        print ("Villain: I am gonna kill you...!")
        input("Press enter to fight>")

        if("gun" in player["items"]):
            print ("You consider your options.")
            print ("options: gun, spider man, iron man")
            pcmd = input(">")

            if(pcmd == "gun"):
                print ("You shot the villain. ")
                print ("But it seems too weak to kill the villain. Ask your friends for help!")
                input(">")
                print ("Do you need help?")
                print (" [ yes, no ] ")
                pcmd = input(">")

                if(pcmd == "yes"):
                    print ("Who wants to help you?")
                    if("ironman" in player["friends"]):
                        print ("spider man, iron man")
                        pcmd = input(">")

                        if (pcmd == "spider man"):
                            print ("Spider-Man tied the villain's body with a spider web.")
                            print ("You shot the villain again!")
                            pcmd = input(">")
                            gameWin()
                        
                        if (pcmd == "iron man"):
                            print ("Iron-Man killed the villain by shooting a beam from his palm. ")
                            pcmd = input(">")
                            gameWin()

                    else:
                        print ("Spider-Man tied the villain's body with a spider web.")
                        print ("You shot the villain again!")
                        pcmd = input(">")
                        gameWin()

                if(pcmd == "no"):
                    print("...")
                    gameOver()
        else:
            print (" Spider-Man has already been attacked. He cannot move now! ")
            print (" The villain is trying to kill you, but you have no weapons. ")
            print (" . . . ")
            input(">")
            gameOver()

def main():
    printGraphic("title") # call the function to print an image
    introStory() # start the intro

main() # this is the first thing that happens
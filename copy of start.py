### this code is was writen by morgan lessard ###
### it also had help from members of the tech with tim discord server ###

### IMPORT'S ###
import time
import random
import sys
### IMPORT'S ###

### CLASSES ####

### PLAYER ###
class Player():
    def __init__(self, **kwargs):
        self.money = 100
        self.in_shop = False  # or 0
        self.at_hotel = False
        self.Location = 1
        self.phase = 1  # to schedule phases of the game and use to see if the player did a quest or has progressed
        self.items = []
        self.Town_1 = 0
        self.Town_2 = 0
        self.Town_3 = 0
        self.Town_4 = 0
        self.Heath = 100
        ### .LOCATION LEGEND ###
            ### 0 = town 1 pre battle ###
            ### 1 = town 1 after battle ###
            ### 2 = route 1 ###
            ### 3 = town 2 pre battle ###
            ### 4 = town 2 after battle ###
            ### 5 = route 2 ###
            ### 6 = town 3 pre battle ###
            ### 7 = town 3 after battle ###
            ### 8 = route 3 ###
            ### 9 = town 4 pre battle ###
            ### 10 = town 4 after battle ###
            ### 11 = ending ###
        ### .LOCATION LEGEND ###
### PLAYER ###

### MAYOR 01 ###
class Mayor01():
    def __init__(self, **kwargs):
        self.Heath = 100
### MAYOR 01 ###

### CLASSES ###

### INIT ###

Player = Player()
Mayor01 = Mayor01()

### INIT ###

########################################################################################################################
########################################################################################################################
########################################################################################################################

### START ###
print("#################################")
print("###   WELCOME TO CELL O MON   ###")
print("#################################")
print("### CREATED BY MORGAN LESSARD ###")
print("###        2019 - 2020        ###")
print("#################################")
print("### IF YOU WANT TO PLAY TYPE  ###")
print("###           'PLAY'          ###")
print("#################################")

answer = input().lower().strip()
time.sleep(2)
### town 1 loop ###
while Player.Location == 0:
    ### BEFORE MAYOR 1 FIGHT CODE ###

    ### true start ###
    if Player.Location == 0:
        print("########################################")
        print("###|               /____/  \        |###")
        print("###|              /     \  /        |###")
        print("###|     o       /| ___ |\/|        |###")
        print("###|    /|\       | | | | /         |###")
        print("###|    /\        |_|_|_|/          |###")
        print("###|................................|###")
        print('########################################')
        print("### welcome to town G1!              ###")
        print('### what would you like to do?       ###')
        print("########################################")
        print("### type 's' to go to the shop       ###")
        print("### type 'h' to go to you house      ###")
        print("### type 'c' to go to G1's mayor     ###")
        print("########################################")

        answer = input()

        ### SHOP CODE ###
        if answer.lower().strip() == "s":
            print("shop")

        ### HOUSE CODE ###
        elif answer.lower().strip() == "h":
            print("########################################")
            print("###|               _ _              |###")
            print("###|              |_|_|             |###")
            print("###|     o        |_|_|             |###")
            print("###|    /|\             _________   |###")
            print("###|    /\               |     |    |###")
            print("###|................................|###")
            print('########################################')
            print("### you enter your house,            ###")
            print('### what would you like to do?       ###')
            print("########################################")
            print("### type 'r' to go to you room       ###")
            print("### type 's' to snack                ###")
            print("### type 'e' to leave                ###")
            print("########################################")

            answer = input()

            ### ROOM CODE ###
            if answer.lower().strip() == "r":
                print("########################################")
                print("###|               _ _              |###")
                print("###|              |_|_|             |###")
                print("###|     o        |_|_|             |###")
                print("###|    /|\              ________|  |###")
                print("###|    /\              | | | | ||  |###")
                print("###|................................|###")
                print('########################################')
                print("### you enter your room,             ###")
                print('### what would you like to do?       ###')
                print("########################################")
                print("### type 's' to sleep                ###")
                print("### type 'g' to collect life savings ###")
                print("### type 'e' to leave                ###")
                print("########################################")

                answer = input()

                ### SLEEP CODE ###
                if answer.lower().strip() == "s":
                    print("sleep")

                ### LIFE SAVINGS CODE ###
                elif answer.lower().strip() == "g":
                    print("you now have 337 gold")

                elif answer.lower().strip() == "e":
                    print("exit")

        ### MAYOR 1 FIGHT CODE ###
        elif answer.lower().strip() == "c":
            print("########################################")
            print("###|               /____/  \        |###")
            print("###|              /     \  /        |###")
            print("###|     o       /| _M_ |\/|        |###")
            print("###|    /|\       | | | | /         |###")
            print("###|    /\        |_|_|_|/          |###")
            print("###|................................|###")
            print('########################################')
            time.sleep(1)
            print("########################################")
            print("###|               /____/  \        |###")
            print("###|              /     \  /        |###")
            print("###|       o     /| _M_ |\/|        |###")
            print("###|      /|\     | | | | /         |###")
            print("###|      /\      |_|_|_|/          |###")
            print("###|................................|###")
            print('########################################')
            time.sleep(1)
            print("########################################")
            print("###|               /____/  \        |###")
            print("###|              /     \  /        |###")
            print("###|         o   /| _M_ |\/|        |###")
            print("###|        /|\   | | | | /         |###")
            print("###|        /\    |_|_|_|/          |###")
            print("###|................................|###")
            print('########################################')
            time.sleep(1)
            print("########################################")
            print("###|               /____/  \        |###")
            print("###|              /     \  /        |###")
            print("###|             /| _M_ |\/|        |###")
            print("###|              | | | | /         |###")
            print("###|              |_|_|_|/          |###")
            print("###|................................|###")
            print('########################################')
            time.sleep(1)
            print("########################################")
            print("###|                                |###")
            print("###|                       o        |###")
            print("###|     o  ______________/|\____   |###")
            print("###|    /|\ | | | | | | | | | | |   |###")
            print("###|    /\                          |###")
            print("###|................................|###")
            print('########################################')
            print("### mayor: you want me to put your   ###")
            print('### cell through G1 of the cell      ###')
            print("### cycle... well you'll have to     ###")
            print("### fight me for it!                 ###")
            print("########################################")
            print("### type 'f' to fight                ###")
            print("### type 'e' to go back to the town  ###")
            print("########################################")

            answer = input()

            if answer == "f":
                print("fight")

            else:
                pass

            while Player.Heath > 0 and Mayor01.Heath > 0:

                print("###########################################")
                print("###| ################################## ###")
                print("###| # mayor - h = ", Mayor01.Heath, "               # ###")
                print("###| ################################## ###")
                print('###|                   o                ###')
                print('###|                  /|\               ###')
                print("###|       o           /\               ###")
                print("###|      /|\                           ###")
                print("###|      /\                            ###")
                print("###| ################################## ###")
                print("###| # you - h = ", Player.Heath, "                # ###")
                print("###| ################################## ###")
                print('###########################################')
                print("### you are fighting the mayor of town  ###")
                print('### G1!                                 ###')
                print("### what would you like to do?          ###")
                print("###########################################")
                print("### type 'a' to attack with your cell   ###")
                print("###########################################")

                answer = input()

                if answer.lower().strip() == "a":
                    def precentage():
                        choice = random.choice(range(1, 100))

                        if choice > 35:
                            print("Your attack was successful!")
                            print("The mayor lost 25 heath!")
                            Mayor01.Heath -= 25
                            time.sleep(2)
                            return True


                        elif choice < 35:
                            print("Your attack missed!")
                            print("The mayor of g1 tried to attack")
                            time.sleep(2)
                            print(" The mayors attack was successful, you lost 25 heath!")
                            Player.Heath -= 25
                            time.sleep(2)
                            return True

                            precentage()
                            print("test 2")
                            ### nothing prints ###
                            return False


                    ### DONT FORGET TO CODE THIS IN ###
                    ### DONT FORGET TO CODE THIS IN ###
                    precentage()
                    ### win code ###
                    if Mayor01.Heath <= 0:
                        print("########################################")
                        print("###|                                |###")
                        print("###|                       o        |###")
                        print("###|     o  ______________/|\____   |###")
                        print("###|    /|\ | | | | | | | | | | |   |###")
                        print("###|    /\                          |###")
                        print("###|................................|###")
                        print('########################################')
                        print("### mayor: you defeated me... guess  ###")
                        print("### ill have to put your cell        ###")
                        print('### through the G1 stage of the cell ###')
                        print("########################################")
                        time.sleep(3)

                        print("########################################")
                        print("###|                                |###")
                        print("###|                       o        |###")
                        print("###|     o  ______________/|\____   |###")
                        print("###|    /|\ | | | | | | | | | | |   |###")
                        print("###|    /\                          |###")
                        print("###|................................|###")
                        print('########################################')
                        print("### mayor: G1 is an intermediate|    ###")
                        print("### phase occupying the time between ###")
                        print('### the end of cell division in      ###')
                        print("### mitosis and the beginning of DNA ###")
                        print("### replication during S phase.      ###")
                        print("### During this time, the cell grows ###")
                        print("### in preparation for DNA           ###")
                        print("### replication, and certain         ###")
                        print("### intracellular components, such   ###")
                        print("### as the centrosomes undergo       ###")
                        print("### replication.                     ###")
                        print("########################################")

                        answer = input("press 'ENTER' to continue...")
                        Player.Town_1 = 1
                    ### lose code ###
                    elif Player.Heath <= 0:
                        print("########################################")
                        print("###|            YOU LOSE            |###")
                        print("########################################")
                        print("### press 'ENTER' to respawn         ###")
                        print("########################################")
                        answer = input()



                else:
                    print("Press a to attack")





### start else ###
### oof exit code ###
else:
    print("oh well... cya!")


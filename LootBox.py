from colorama import Fore
import random
import pygame

#class Legendery_Crate:
 #      def __init__():
  #            Legendery_Crate.Weights = ()


#class Epic_Crate:


#class Rare_Crate:

        
#class Uncommon_Crate:
       

class Common_Crate: 
      Weights = (80,15,1,0.9,0.1)

pygame. init()
Collection_Sound = pygame.mixer.Sound('/home/jay-phoenix/Downloads/Ding - Sound Effect (HD).mp3')

#MENU
def Username_Selection():
    #Asks for a username and opens a txt file, if username not recognised then either asks if they wish to make one, or opens anonymous
    global Username
    Username = input('what is your username?')
    Usernames = (r'Usernames.txt')
    
    #checks selected username against txt file
    with open(Usernames, 'rt') as f:
        text = f.readline()
        text = text.strip().split()
        
    #if it is is txt file, it carries on
    if Username in text:
        print('Welcome', Username)
        User_Data = open(Username, 'a')
        menu()
    #if not in txt file, asks if it wants to create one or opens the anonymous
    elif Username not in text:
        Choice = input('Would you like to create a new profile?')
        if Choice in ('Y', 'yes', 'YES', 'y'):
            f = open('Usernames.txt', 'a')
            f.write(Username)
            User_Data = open(Username, 'a')
            print('Welcome', Username)
            menu()
        elif Choice in('N', 'n', 'No', 'NO', ' no'):
            User_Data = open('Anonymous.txt', 'a')
            menu()
            
        else:
            print('error')
            Username_Selection()

def menu():
    start = input ('do you want to open a loot box')
    if start in ('Y', 'yes', 'y', 'YES', 'Yes'):
        lootbox_opening()
    elif start in ('N', 'n', 'No', 'NO', 'no'):
        quit()
    else:
        print('error')
        menu()
crate_number = 1



#Opening the lootbox
def lootbox_opening():
    #sets up the first set of spins
    Crate_Type = input('what type of crate you want to open?')
    Number_Off_Spins = input('how many times would you like to spin')

    if Number_Off_Spins in ['1','2','3','4','5','6','7','8','9','10']:
        Number_Off_Spins = int(Number_Off_Spins)
    else:
        print('error')
        lootbox_opening()

    if Crate_Type == 'Common':
        TypeOfItem = random.choices(['Common','Uncommon','Rare','Epic','Legendery'], weights = (Common_Crate.Weights))
        TypeOfItem = ''.join(TypeOfItem)
        print(TypeOfItem)

        if TypeOfItem == 'Common':
            for i in range(Number_Off_Spins):
                Item_Type = Common_Crate()
                chosen_item = random.choices(open('Common_items.txt').readlines())
                print(Fore.BLUE + 'opening crate', '\n...')
                chosen_item = ''.join(chosen_item)
                Collection_Sound.play()
                User_Data = open(Username, 'a')
                User_Data.write('\n')
                User_Data.write(chosen_item)
                print('congratulations, you just won a:', Fore.RED + chosen_item)

    start_again = input(Fore.RESET + 'would you like to spin it again?')
    #decides on whether or not it activates again
    if start_again in ('Y', 'yes', 'y', 'YES', 'Yes'):
       lootbox_opening()
    elif start_again in ('N', 'n', 'No', 'NO', 'no'):
        menu()
    else:
        print('error, returning to main menu')
        menu()


Username_Selection()
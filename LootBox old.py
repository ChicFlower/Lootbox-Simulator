from colorama import Fore
import random
# import pygame

class Legendery_Crate:
    Weights = ()



class Epic_Crate:
    Weights = ()

class Rare_Crate:
    Weights = ()

class Uncommon_Crate:
    Weights = (60,35)

class Common_Crate: 
    Weights = (80,15,5,0.9,0.1)

# pygame. init()
# Collection_Sound = pygame.mixer.Sound('/home/jay-phoenix/Downloads/Ding - Sound Effect (HD).mp3')
username = ""
#MENU
def Username_Selection():
    #Asks for a username and opens a txt file, if username not recognised then either asks if they wish to make one, or opens anonymous
    
    username = input('what is your username?')
    Usernames = (r'Usernames.txt')
    
    #checks selected username against txt file
    with open(Usernames, 'rt') as f:
        text = f.readline()
        text = text.strip().split()
        
    #if it is is txt file, it carries on
    if username in text:
        print('Welcome', username)
        User_Data = open(username, 'a')
        menu()
    #if not in txt file, asks if it wants to create one or opens the anonymous
    elif username not in text:
        Choice = input('Would you like to create a new profile?')
        if Choice in ('Y', 'yes', 'YES', 'y'):
            f = open('Usernames.txt', 'a')
            f.write(username)
            User_Data = open(username, 'a')
            print('Welcome', username)
            menu()
        elif Choice in('N', 'n', 'No', 'NO', ' no'):
            User_Data = open('Anonymous.txt', 'a')
            menu()
            
        else:
            print('error')
            Username_Selection()

def menu():
    start = input ('do you want to open a loot box').lower()
    if start in ('yes', 'y'):
        lootbox_opening()
    elif start in ('n', 'no'):
        quit()
    else:
        print('error')
        menu()

crate_number = 1

def Congratulations():
    global chosen_item
    chosen_item = ''.join(chosen_item)
    # Collection_Sound.play()
    User_Data = open(username, 'a')
    User_Data.write('\n')
    User_Data.write(chosen_item)
    print('congratulations, you just won a:', Fore.RED + chosen_item)

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
        TypeOfItem = random.choices(['Common','Uncommon','Rare','Epic','Legendary'], weights = (Common_Crate.Weights))
        TypeOfItem = ''.join(TypeOfItem)
        print(TypeOfItem)
    elif Crate_Type == 'Uncommon':
        TypeOfItem = random.choices(['Common','Uncommon','Rare','Epic','Legendary'], weights = (Uncommon_Crate.Weights))
        TypeOfItem = ''.join(TypeOfItem)
        print(TypeOfItem)    
    elif Crate_Type == 'Rare':
        TypeOfItem = random.choices(['Common','Uncommon','Rare','Epic','Legendary'], weights = (Rare_Crate.Weights))
        TypeOfItem = ''.join(TypeOfItem)
        print(TypeOfItem)            
    elif Crate_Type == 'Epic':
        TypeOfItem = random.choices(['Common','Uncommon','Rare','Epic','Legendary'], weights = (Epic_Crate.Weights))
        TypeOfItem = ''.join(TypeOfItem)
        print(TypeOfItem)   
    elif Crate_Type == 'Legendary':
        TypeOfItem = random.choices(['Common','Uncommon','Rare','Epic','Legendary'], weights = (Legendery_Crate.Weights))
        TypeOfItem = ''.join(TypeOfItem)
        print(TypeOfItem)



    if TypeOfItem == 'Common':
        global chosen_item
        for i in range(Number_Off_Spins):
            Item_Type = Common_Crate()
            chosen_item = random.choices(open('Common_items.txt').readlines())
            print(Fore.BLUE + 'opening crate', '\n...')
            Congratulations()


    elif TypeOfItem == 'Uncommon':
        for i in range(Number_Off_Spins):
            Item_Type = Uncommon_Crate()
            chosen_item = random.choices(open('Uncommon_items.txt').readlines())
            print(Fore.BLUE + 'opening crate', '\n...')
            Congratulations()


    elif TypeOfItem == 'Rare':
        for i in range(Number_Off_Spins):
            Item_Type = Rare_Crate()
            chosen_item = random.choices(open('Rare_items.txt').readlines())
            print(Fore.BLUE + 'opening crate', '\n...')
            Congratulations()


    elif TypeOfItem == 'Epic':
        for i in range(Number_Off_Spins):
            Item_Type = Epic_Crate()
            print(Fore.BLUE + 'opening crate', '\n...')
            Congratulations()


    elif TypeOfItem == 'Legendary':
        for i in range(Number_Off_Spins):
            Item_Type = Epic_Crate()
            print(Fore.BLUE + 'opening crate', '\n...')
            Congratulations()

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
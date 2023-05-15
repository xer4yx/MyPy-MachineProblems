"""

                                                                MACHINE PROBLEM 3 & 4: CLASSES AND OBJECTS
                                                PROJECT CREATED BY:
                                                - Angelo Bicomong (Github: xer4yx)
                                                - Jonner Villapando (Github: nnerr)

"""
import os
from undeadClass import *

undead_list = []

def mainMenu():
    os.system('cls')
    print("""
          UNDEAD MAIN MENU
        [1] CREATE UNDEAD
        [2] COMMAND UNDEAD
        [3] DISPLAY UNDEAD
        [4] EXIT PROGRAM
        """)


def createMenu():
    os.system('cls')
    print("""
          CHOOSE WHAT TYPE OF UNDEAD YOU WANT TO CREATE
        [1] Zombie
        [2] Vampire
        [3] Skeleton
        [4] Ghost
        [5] Lich
        [6] Mummy
              
                """)
    choice = int(input("Select what type you want to create: "))
    name = input("Name your undead: ")
    os.system('cls')
    if name == '':
        name = None

    if choice == 1:
        undead_list.append(Zombie(name))

    elif choice == 2:
        undead_list.append(Vampire(name))

    elif choice == 3:
        undead_list.append(Skeleton(name))

    elif choice == 4:
        undead_list.append(Ghost(name))

    elif choice == 5:
        undead_list.append(Lich(name))

    elif choice == 6:
        undead_list.append(Mummy(name))
    else:
        print("Unknown input, try again")
    print("")


def commandMenu():
    os.system('cls')
    print("""
          Command Undead - please select an undead to issue a command to
          """)
    for index, obj in enumerate(undead_list):
        print(f'\t[{index + 1}] {obj.getName()}')
    print("")
    selected = int(input("Choice: "))
    selected -= 1
    os.system('cls')
    print(f"""
          {undead_list[selected].getName()}'s available abilities:
          """)
    for index, ability in enumerate(undead_list[selected].getAbility()):
        print(f'\t[{index + 1}] {ability}')
    print("")
    command = int(input("Select a command to issue: "))
    command = undead_list[selected].getAbility()[command - 1]
    os.system('cls')
    if not command == "Revive":
        print("""
          Use on which undead?
          """)
        for index, obj in enumerate(undead_list):
            if not (selected == index):
                print(f'\t[{index + 1}] {obj.getName()}')
        print("")
        enemy = int(input("Choice: "))
        enemy -= 1
        os.system('cls')
    if command == "Attack":
        print(
            f'{undead_list[enemy].getName()}\'s Health: {undead_list[enemy].getHP()}')
        print(
            f'{undead_list[selected].getName()} attacked {undead_list[enemy].getName()}')
        undead_list[selected].Attack(undead_list[enemy])
        print(
            f'{undead_list[enemy].getName()}\'s Health: {undead_list[enemy].getHP()}')
    elif command == "Munch":
        print(
            f'{undead_list[selected].getName()}\'s Health: {undead_list[selected].getHP()}')
        print(
            f'{undead_list[selected].getName()} eats {undead_list[enemy].getName()}')
        undead_list[selected].Munch(undead_list[enemy])
        print(
            f'{undead_list[selected].getName()}\'s Health: {undead_list[selected].getHP()}')
    elif command == "Bite":
        print(
            f'{undead_list[selected].getName()}\'s Health: {undead_list[selected].getHP()}')
        print(
            f'{undead_list[selected].getName()} bites {undead_list[enemy].getName()}')
        undead_list[selected].Bite(undead_list[enemy])
        print(
            f'{undead_list[selected].getName()}\'s Health: {undead_list[selected].getHP()}')
    elif command == "Haunt":
        print(
            f'{undead_list[selected].getName()}\'s Health: {undead_list[selected].getHP()}')
        print(
            f'{undead_list[selected].getName()} haunts {undead_list[enemy].getName()}')
        undead_list[selected].Haunt(undead_list[enemy])
        print(
            f'{undead_list[selected].getName()}\'s Health: {undead_list[selected].getHP()}')
    elif command == "Spellvamp":
        print(
            f'{undead_list[selected].getName()}\'s Health: {undead_list[selected].getHP()}')
        print(
            f'{undead_list[enemy].getName()}\'s Health: {undead_list[enemy].getHP()}')
        print(
            f'{undead_list[selected].getName()} casts a spell on {undead_list[enemy].getName()}')
        undead_list[selected].SpellVamp(undead_list[enemy])
        print(
            f'{undead_list[selected].getName()}\'s Health: {undead_list[selected].getHP()}')
        print(
            f'{undead_list[enemy].getName()}\'s Health: {undead_list[enemy].getHP()}')
    elif command == "Revive":
        print(
            f'{undead_list[selected].getName()}\'s State: {"dead" if undead_list[selected].isDead() else "alive"}')
        print(f'{undead_list[selected].getName()} tries to revive')
        undead_list[selected].Revive()
        print(
            f'{undead_list[selected].getName()}\'s State: {"dead" if undead_list[selected].isDead() else "alive"}')
    else:
        print("Invalid input")
    print("")

def displayMenu():
    os.system('cls')
    print("       UNDEAD INDEX")
    for obj in undead_list:
        print("")
        obj.DisplayStat()
    print("")



# Won't be using unless the program meets requirements
if __name__ == "__main__":
    while True:
        mainMenu()
        choice = int(input("Enter your choice: "))

        match choice:
            case 1:
                createMenu()
                buffer = input("Press <ENTER> to continue...")
            case 2:
                commandMenu()
                buffer = input("Press <ENTER> to continue...")
            case 3:
                os.system('cls')
                displayMenu()
                buffer = input("Press <ENTER> to continue...")
            case 4:
                os.system('cls')
                exit()
            case other:
                print("Invalid choice")

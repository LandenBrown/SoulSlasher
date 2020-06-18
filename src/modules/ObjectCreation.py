#This is where we will create the object creation for use
# ALOT of our customization and procedural generation work will be done here
# Importing required class modules - it's important we always only import WHAT WE NEED.
from .PlayerClass import Monster #<-- This will need to be changed to the multiple modules that we separate out. 
from .PlayerClass import Player #<-- importing Player class
#Test monster creation - rough dev testing only - to be used in BattleComponent.py
def createTestMonster():
    print("Would you like to create a 1.Wolf\n2.Salamander\n3.Ogre\n4.Golem")
    monsterChoice = ""
    if monsterChoice == "1":
        monster = Monster("Wolf", "Small", "None", 10, 5)
        return monster
    elif monsterChoice == "2":
        monster = Monster("Salamander", "Medium", "None", 30, 10)
        return monster
    elif monsterChoice == "3":
        monster = Monster("Ogre", "Large", "None", 50, 20)
        return monster
    elif monsterChoice == "4":
        monster = Monster("Golem", "Collosus", "None", 100, 35)
        return monster
def createTestPlayer():
    print("What level would you like to be?")
    playerLevel = input()
    #Run level/hp calculation
    print("Would you like to be close to leveling? 1.no\n2.yes")
    closeToLevel = input()
    print("Weapon? 1.Great Axe\n2.Great Sword\n3.Great Spear")
    playerWeapon = input()
    #print("Skipping Aura...")




#Creating Static Player


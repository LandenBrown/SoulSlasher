#This is where we will create the object creation for use
# ALOT of our customization and procedural generation work will be done here
# Importing required class modules - it's important we always only import WHAT WE NEED.
import PlayerClass as PC #<-- This will need to be changed to the multiple modules that we separate out.
#<-- importing Player class
#Test monster creation - rough dev testing only - to be used in BattleComponent.py
def createTestMonster():
    print("Would you like to create a 1.Wolf\n2.Salamander\n3.Ogre\n4.Golem")
    monsterChoice = input()
    if monsterChoice == "1":
        monster = PC.Monster("Wolf", "Small", "None", 10, 5)
        return monster
    elif monsterChoice == "2":
        monster = PC.Monster("Salamander", "Medium", "None", 30, 10)
        return monster
    elif monsterChoice == "3":
        monster = PC.Monster("Ogre", "Large", "None", 50, 20)
        return monster
    elif monsterChoice == "4":
        monster = PC.Monster("Golem", "Collosus", "None", 100, 35)
        return monster

#Creating a dev test player
def createTestPlayer():
    testPlayer = PC.Player("test", 0, 0, None, None, None, None, None, 0, 0, None, None)
    print("What level would you like to be?")
    testPlayer.level = int(input())
    #Run level/hp calculation 
    testPlayer.levelCheck()
    #Testing level up functionality
    print("Would you like to be close to leveling? 1.no\n2.yes")
    closeToLevel = input()
    if closeToLevel == "2":
        testPlayer.goalXP = testPlayer.goalXP - 1
    #player weapon selection
    print("Weapon? 1.Great Axe\n2.Great Sword\n3.Great Spear")
    #testPlayer.weapon = createTestweapon()
    #print("Skipping Aura...")
    

#Creating dev test weapons
def createTestweapon():
    weaponchoice = ""
    #(name, type, damage, element)
    if weaponchoice == "1":
        weapon = weapon("Great Axe", "Axe", 10, "none")
    if weaponchoice == "2":
        weapon = weapon("Great Sword", "Sword", 10, "none") 
    if weaponchoice == "3":
        weapon = weapon("Great Spear", "Spear", 10, "none")


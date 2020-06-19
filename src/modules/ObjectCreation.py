#This is where we will create the object creation for use
# ALOT of our customization and procedural generation work will be done here
# Importing required class modules - it's important we always only import WHAT WE NEED.
import PlayerClass #<-- This will need to be changed to the multiple modules that we separate out.
#<-- importing Player class
#Test monster creation - rough dev testing only - to be used in BattleComponent.py
def createTestMonster():
    print("Would you like to create a \n1.Wolf\n2.Salamander\n3.Ogre\n4.Golem")
    monsterChoice = input()
    if monsterChoice == "1":
        monster = PlayerClass.Monster("Wolf", "Small", "None", 10, 5, 1)
        return monster
    elif monsterChoice == "2":
        monster = PlayerClass.Monster("Salamander", "Medium", "None", 30, 10, 1)
        return monster
    elif monsterChoice == "3":
        monster = PlayerClass.Monster("Ogre", "Large", "None", 50, 20, 1)
        return monster
    elif monsterChoice == "4":
        monster = PlayerClass.Monster("Golem", "Collosus", "None", 100, 35, 1)
        return monster
#test
#Creating a dev test player
def createTestPlayer():
    testPlayer = PlayerClass.Player("test", 10, 10, 10, None, None, None, None, None, 0, 10, None, 1)
    print("What level would you like to be?")
    desiredLevel = int(input())
    #Run level/hp calculation
    for i in range(desiredLevel-1):
        print("Leveling up...")
        testPlayer.currentXp = testPlayer.goalXp
        testPlayer.levelCheck()
        print("You are now level "+str(testPlayer.level))
    #Testing level up functionality
    print("Would you like to be close to leveling?\n1.no\n2.yes")
    closeToLevel = input()
    if closeToLevel == "2":
        testPlayer.currentXp = testPlayer.goalXp - 1
        print("You are now close to leveling...")
    #player weapon selection
    print("Weapon?\n1.Great Axe\n2.Great Sword\n3.Great Spear")
    testPlayer.weapon = createTestweapon()
    return testPlayer
    #print("Skipping Aura...")
    

#Creating dev test weapons
def createTestweapon():
    weaponchoice = input()
    #(name, type, damage, element)
    if weaponchoice == "1":
        weapon = PlayerClass.Weapon("Great Axe", "Axe", 10, "none", None)
        return weapon   
    if weaponchoice == "2":
        weapon = PlayerClass.Weapon("Great Sword", "Sword", 10, "none", None) 
        return weapon
    if weaponchoice == "3":
        weapon = PlayerClass.Weapon("Great Spear", "Spear", 10, "none", None)
        return weapon



#Create dropped item from mob - createDroppedItem()
#When a mob is killed we will create and return an object
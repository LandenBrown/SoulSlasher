#This is where we will create the object creation for use
# ALOT of our customization and procedural generation work will be done here
# Importing required class modules - it's important we always only import WHAT WE NEED.
from modules import PlayerClass #<-- This will need to be changed to the multiple modules that we separate out.
#<-- importing Player class
#Test monster creation - rough dev testing only - to be used in BattleComponent.py
import time
#### Drop Tables
#Flesh
fleshDrops = ["Hide", "Fur", "Scale", "Bone", "Claw"]
#Sea
seaDrops = ["Shell", "Bone", "Fin", "Scale"]
#Brute
bruteDrops = ["Strong Hide", "Large Scale", "Large Bone", "Sharp Claw"]
#Metal
metalDrops = ["Iron", "Steel", "Damascus"]


###### AREAS ######
testArea1 = PlayerClass.Area("Test Area 1", None, None, None, None)
testArea2 = PlayerClass.Area("Test Area 2", None, None, None, None)
testArea3 = PlayerClass.Area("Test Area 3", None, None, None, None)

def area_Initialization_Script():
    print("nothing yet")
    #Area 1
    testArea1.nextArea = testArea2
    #Area 2
    testArea2.previousArea = testArea1
    testArea2.previousArea = testArea2
    #Area 3
    testArea3.previousArea = testArea2

def selectMonsterTypeDropTable(targetMonster):
    if targetMonster.monsterType == "Flesh":
        return fleshDrops
    elif targetMonster.monsterType == "Sea":
        return seaDrops
    elif targetMonster.monsterType == "Brute":
        return bruteDrops
    elif targetMonster.monsterType == "Metal":
        return metalDrops


def createTestMonster():
    print("Would you like to create a \n1.Wolf\n2.Salamander\n3.Ogre\n4.Golem")
    monsterChoice = input()
    if monsterChoice == "1":
        monster = PlayerClass.Monster("Wolf", "Small", "None", 10, 10, 5, 1, None, 1, "Flesh")
    elif monsterChoice == "2":
        monster = PlayerClass.Monster("Salamander", "Medium", "None", 30, 30, 10, 1, None, 3, "Sea")
    elif monsterChoice == "3":
        monster = PlayerClass.Monster("Ogre", "Large", "None", 50, 50, 20, 1, None, 5, "Brute")
    elif monsterChoice == "4":
        monster = PlayerClass.Monster("Golem", "Collosus", "None", 100, 100, 35, 1, None, 9, "Metal")
    
    monster.dropTable = selectMonsterTypeDropTable(monster)
    return monster
#test
#Creating a dev test player
def createTestPlayer():
    testPlayer = PlayerClass.Player("test", 10, 10, 10, None, None, None, None, None, 0, 10, None, 1)
    testPlayer.armor = createTestArmor() #create player's armor
    testPlayer.armor.element = createTestElement() #create armor element
    testPlayer.pet = createTestPet() #create player's pet
    testPlayer.aura = createTestAura() #create player's aura


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
    testPlayer.weapon = createTestweapon() #Creating test weapon
    return testPlayer

    #print("Skipping Aura...")
    

#Creating dev test weapons
def createTestweapon():
    print("Weapon?\n1.Great Axe\n2.Great Sword\n3.Great Spear")
    weaponchoice = input()
    #(name, type, damage, element)
    if weaponchoice == "1":
        weapon = PlayerClass.Weapon("Great Axe", "Axe", 10, "none")
        weapon.element = createTestElement()
        return weapon
    if weaponchoice == "2":
        weapon = PlayerClass.Weapon("Great Sword", "Sword", 10, "none")
        weapon.element = createTestElement() 
        return weapon
    if weaponchoice == "3":
        weapon = PlayerClass.Weapon("Great Spear", "Spear", 10, "none")
        weapon.element = createTestElement()
        return weapon


#Generate test pet for combat sequencing
def createTestPet():
    testPet = PlayerClass.Pet("Bee", "Small", None, 30, 30, 4)
    return testPet

#creating a test Aura for attribute modication testing
def createTestAura():
    testAura = PlayerClass.Aura("Demonic Visage", 5, 0)
    return testAura
    #Need to add this to player.CheckBonuses()


#creating test armor for attribute modification testing
def createTestArmor():
    testArmor = PlayerClass.Armor("Ogre Hide Armor", 3, None)
    return testArmor


def createTestElement():
    testElement = PlayerClass.Element("Minor Element", "Divine", 4, 4)
    return testElement


####Crafting Recipes#####



#Create dropped item from mob - createDroppedItem()
#When a mob is killed we will create and return an object

#importing our dev-only monster and player creation functions, from ObjectCreation.py
#because Monster and Player are alreay imported in ObjectCreation.py
#we dont want to use a wildcard (import * / import "all"), because it will double back
#and import those base classes too, which we don't need, we just need the functions.
import ObjectCreation

def BattleMenu():
    print("This is coming soon...")

def TestBattleSequence():
    #Generating Monster
    testMonster = ObjectCreation.createTestMonster()
    print("\nMonster Attributes:")
    print("Monster: " + testMonster.name)
    print("Size: " + testMonster.size)
    print("HP: " + str(testMonster.hp))
    
    #Generate Player
    testPlayer = ObjectCreation.createTestPlayer()

    #Printing out player attributes
    print("Level: "+str(testPlayer.level))
    print("HP: "+str(testPlayer.hp)+"/"+str(testPlayer.maxHp))
    print("Weapon: "+testPlayer.weapon.name+" / Damage: "+str(testPlayer.weapon.damage))
    print("Experience: " +str(testPlayer.currentXp)+"/"+str(testPlayer.goalXp))
    print("Current Pet: "+testPlayer.monsters.name)

    


TestBattleSequence()

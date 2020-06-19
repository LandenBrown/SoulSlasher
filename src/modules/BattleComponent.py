#importing our dev-only monster and player creation functions, from ObjectCreation.py
#because Monster and Player are alreay imported in ObjectCreation.py
#we dont want to use a wildcard (import * / import "all"), because it will double back
#and import those base classes too, which we don't need, we just need the functions.
import ObjectCreation

def startBattle(player, pet, monster):
    print("You have encountered a " + monster.size + " " + monster.name +"!")
    #ccreate battle choices based off weapon type
    #create monster specific attacks and randomize use and outcome
    while player.hp > 0:
        print("What would you like to do?")
        #create monster.attack(target) - DONE
        #create player.attack(target) - DONE
        #create player.pet.attack(target) - DONE


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


    #start battle sequence
    startBattle(testPlayer, testPlayer.monsters, testMonster)


TestBattleSequence()

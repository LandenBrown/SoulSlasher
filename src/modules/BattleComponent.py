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
        print("Player: " + str(player.hp) + "/" + str(player.maxHp))
        print("Monster: " + str(monster.hp) + "/" + str(monster.maxHp))
        #create monster.attack(target) - DONE
        #create player.attack(target) - DONE
        #create player.pet.attack(target) - DONE
        print("press 1 to attack")
        attackChoice = input()
        if attackChoice == "1":
            player.attack(monster)

        #ensure player didn't kill monster
        if monster.hp > 0:
            print("The monster is now attacking!")
            monster.attack(player)
            #check to see if monster killed player
            if player.hp < 0:
                print("You have died!")
                break
        else:
            print("You have killed the monster!")
            break
        #check to ensure pet isn't dead
        if pet.hp > 0:
            print("Your pet is attacking!")
            pet.attack(monster)
            #check to see if pet killed monster
            if monster.hp < 0:
                print("Your pet has killed the monster")
                break
        else:
            print("Your pet is dead and cannot attack!")





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

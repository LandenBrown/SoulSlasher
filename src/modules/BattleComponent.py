#importing our dev-only monster and player creation functions, from ObjectCreation.py
#because Monster and Player are alreay imported in ObjectCreation.py
#we dont want to use a wildcard (import * / import "all"), because it will double back
#and import those base classes too, which we don't need, we just need the functions.
import ObjectCreation

def BattleMenu():
    print("This is coming soon...")

def TestBattleSequence():
    testMonster = ObjectCreation.createTestMonster()
    print(testMonster.name)
    print(testMonster.size)
    print(str(testMonster.hp))

TestBattleSequence()

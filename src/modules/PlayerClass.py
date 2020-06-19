import time
class Player:
    def __init__(self, name, hp, baseMaxHp, maxHp, weapon, armor, aura, pet, inventory, currentXp, goalXp, area, level):
        self.name = name
        self.hp = hp
        self.maxHp = maxHp
        self.baseMaxHp = baseMaxHp
        self.weapon = weapon
        self.armor = armor
        self.aura = aura
        self.pet = pet
        self.inventory = inventory
        self.currentXp = currentXp
        self.goalXp = goalXp
        self.area = area
        self.level = level


    #need to create a MaxHP check to check for all item bonuses - THIS WILL NEED WORK AS WE CREATE ELEMENTS, ETC
    def checkBonuses(self):
        #the values in here are placeholders and this function will 100% fail if ran in current state. DO NOT USE YET.
        #self.maxHp = self.baseMaxHp + (self.aura.hpBonus + self.armor.hpBonus)
        self.maxHp = self.baseMaxHp
        #healing health back to full after check
        self.hp = self.maxHp

    #should work for all levels, no need to draw it out for each level. This means that there is no level cap
    def levelCheck(self):
        print("Starting level check...")
        time.sleep(0.5)
        if self.currentXp >= self.goalXp:
            self.goalXp = int(self.goalXp*1.15)
            self.baseMaxHp = int(self.baseMaxHp*1.35)
            self.level += 1
            self.currentXp = 0
            self.checkBonuses()

    def attack(self, target):
        print("You are attacking!")
        target.hp = target.hp - self.weapon.damage
        print(self.name + " did " + str(self.weapon.damage) + " damage!")


        #level -> HP calculation 
        #level -> goalXP calculation

class Monster:
    def __init__(self, name, size, element, hp, xpReward, level, dropTable, damage):
        self.name = name
        self.size = size
        self.element = element
        self.hp = hp
        self.xpReward = xpReward
        self.level = level
        self.dropTable = dropTable
        self.damage = damage
    def attack(self, target):
        print(self.name + " is attacking!")
        target.hp = target.hp - self.damage
        print(self.name + " did " + str(self.damage) + " damage!")

class Weapon:
    def __init__(self, name, weaponType, damage, element):
        self.name = name
        self.weaponType = weaponType
        self.damage = damage
        self.element = element

class Armor:
    def __init__(self, name, defense, element):    
        self.name = name 
        self.defense = defense
        self.element = element

class Aura:
    def __init__(self, name, hpBonus, defenseBonus, attackBonus):  
        self.name = name 
        self.hpBonus = hpBonus
        self.defenseBonus = defenseBonus
        self.attackBonus = attackBonus

class Element:
    def __init__(self, name, elementType):
        self.name = name 
        self.elementType = elementType    

class Pet:
    def __init__(self, name, size, element, hp, maxHp, damage):
        self.name = name
        self.size = size
        self.element = element 
        self.hp = hp
        self.maxHp = maxHp
        self.damage = damage
    def attack(self, target):
        print("Pet " + self.name + " is attacking!")
        target.hp = target.hp - self.damage
        print("Pet " + self.name + " did " + str(self.damage) + " damage!")


class Loot_Item:
    def __init__(self, name, lootType, price):
        self.name = name
        self.lootType = lootType
        self.price = price


        
    
    
    
    #name, type, price
    #
    #BS DONT USE - random 100 - <80 common OR <50 rare <20 legendary
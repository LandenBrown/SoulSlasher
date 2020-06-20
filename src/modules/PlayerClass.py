import time
#####
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
        #Need to check bonuses of crafted elements on the armor
        armorBonus = self.armor.checkBonuses()
        #print("ARMOR BONUS: " + str(armorBonus))
        auraBonus = self.aura.hpBonus
        #print("AURA BONUS: " + str(auraBonus))
        addedBonuses = armorBonus + auraBonus
        #print("ADDED BONUSES: " + str(addedBonuses))
        #time.sleep(0.5)
        self.maxHp = self.baseMaxHp + addedBonuses #Calculating all bonuses
        #print("MaxHP: " + str(self.maxHp) + " / baseMaxHP" + str(self.baseMaxHp))
        #DONT NEED THE BELOW, LOGIC WAS CAUSING THE LEVEL CHECK TO INCREASE THE HEALTH WITH BONUSES INCLUDED (10+4+4)*1.35
        #self.maxHp = self.baseMaxHp #Setting maxHp to our total health+Bonus value (baseMaxHp)
        #healing health back to full after check
        self.hp = self.maxHp


    #should work for all levels, no need to draw it out for each level. This means that there is no level cap
    def levelCheck(self):
        #print("Starting level check...")
        #time.sleep(0.1)
        if self.currentXp >= self.goalXp:
            self.goalXp = int(self.goalXp*1.15)
            #print("current base hp: " + str(self.baseMaxHp))
            #time.sleep(.5)
            self.baseMaxHp = int(self.baseMaxHp*1.35)
            #print("new base hp: " + str(self.baseMaxHp))
            #time.sleep(.5)
            self.level += 1
            self.currentXp = 0
            self.checkBonuses()

    def attack(self, target):
        print("You are attacking!")
        target.hp = target.hp - self.weapon.damage
        print(self.name + " did " + str(self.weapon.damage) + " damage!")


        #level -> HP calculation 
        #level -> goalXP calculation

#####
class Monster:
    def __init__(self, name, size, element, hp, maxHp, xpReward, level, dropTable, damage, monsterType):
        self.name = name
        self.size = size
        self.element = element
        self.hp = hp
        self.maxHp = maxHp
        self.xpReward = xpReward
        self.level = level
        self.dropTable = dropTable
        self.damage = damage
        self.monsterType = monsterType
    def attack(self, target):
        print(self.name + " is attacking!")
        target.hp = target.hp - self.damage
        print(self.name + " did " + str(self.damage) + " damage!")

#####
class Weapon:
    def __init__(self, name, weaponType, damage, element):
        self.name = name
        self.weaponType = weaponType
        self.damage = damage
        self.element = element


#####
class Armor:
    def __init__(self, name, hpBonus, element):    
        self.name = name 
        self.hpBonus = hpBonus
        self.element = element

    def checkBonuses(self):
        bonusTotal = self.hpBonus + self.element.hpBonus
        return bonusTotal
        #Armor just checks HP bonus, Weapon will check for attack bonus. 
        # We will wrap both of these in their respective classes  

#####
class Aura:
    def __init__(self, name, hpBonus, attackBonus):  
        self.name = name 
        self.hpBonus = hpBonus
        self.attackBonus = attackBonus

#####
class Element:
    def __init__(self, name, elementType, hpBonus, attackBonus):
        self.name = name 
        self.elementType = elementType
        self.hpBonus = hpBonus
        self.attackBonus = attackBonus

#####
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

#####
class Loot_Item:
    def __init__(self, name, lootType, price):
        self.name = name
        self.lootType = lootType
        self.price = price

class Area:
    def __init__(self, name, previousArea, nextArea, forge, shop):
        self.name = name
        self.previousArea = previousArea
        self.nextArea = nextArea
        self.forge = forge
        self.shop = shop

        
    
    
    
    #name, type, price
    #
    #BS DONT USE - random 100 - <80 common OR <50 rare <20 legendary
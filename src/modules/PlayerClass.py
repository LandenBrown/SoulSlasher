import time
class Player:
    def __init__(self, name, hp, baseMaxHp, maxHp, weapon, armor, aura, monsters, inventory, currentXp, goalXp, area, level):
        self.name = name
        self.hp = hp
        self.maxHp = maxHp
        self.baseMaxHp = baseMaxHp
        self.weapon = weapon
        self.armor = armor
        self.aura = aura
        self.monsters = monsters
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


        #level -> HP calculation 
        #level -> goalXP calculation

class Monster:
    def __init__(self, name, size, element, hp, xpReward, level):
        self.name = name
        self.size = size
        self.element = element
        self.hp = hp
        self.xpReward = xpReward
        self.level = level

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
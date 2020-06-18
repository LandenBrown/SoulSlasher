class Player:
    def __init__(self, name, hp, maxHP, weapon, armor, aura, monsters, inventory, currentXP, goalXP, area):
        self.name = name
        self.hp = hp
        self.maxhp = maxHP
        self.weapon = weapon
        self.armor = armor
        self.aura = aura
        self.monsters = monsters
        self.inventory = inventory
        self.currentXP = currentXP
        self.goalXP = goalXP
        self.area = area

        #level -> HP calculation 
        #level -> goalXP calculation

class Monster:
    def __init__(self, name, size, element, hp, xpReward):
        self.name = name
        self.size = size
        self.element = element
        self.hp = hp
        self.xpReward = xpReward

class Weapon:
    def __init__(self, name, Type, damage, element):
        self.name = name
        self.Type = Type
        self.damage = damage
        self. element = element

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
    def __init__(self, name, type):
        self.name = name 
        self.type = type         
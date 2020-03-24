"""Fantasy Fight Project

-- Version 0.1
Author : Sophie Blanchard
Purpose : simple fight game with fantasy characters
Start date : 03-17-2020
Last update : 03-24-2020

This file contains the classes :
- Character and its subclass Player
- Shop
- Weapon and its subclass Spell
- Armour

It also contains the constants needed to initialize class instances.

"""

import random

# Constants used to initialize characters

MALE_NAMES = ['Albert', 'Kronos', 'Alec', 'Bran', 'Urtuk', 'Shun']
FEMALE_NAMES = ['Lydia', 'Tulie', 'Aimee', 'Selene', 'Kira', 'Ksyncix']
OTHER_NAMES = ['Al', 'Effen', 'Juno', 'Lerrewen', 'Gorgo', 'Jviz']
GENDERS = ['Male', 'Female', 'Other']
RACES = ['Githzerai', 'Rakshasa', 'Illithid', 'Tieflin', 'Banshee']
ABILITIES = {'Githzerai': {'name': 'Vicious Swash', 'damage_min': -10, 'damage_max': 10},
             'Rakshasa': {'name': 'Subjugate', 'damage_min': -10, 'damage_max': 10},
             'Illithid': {'name': 'Mind pump', 'damage_min': -10, 'damage_max': 10},
             'Tieflin': {'name': 'Sting whip', 'damage_min': -10, 'damage_max': 10},
             'Banshee': {'name': 'Scream', 'damage_min': -10, 'damage_max': 10}}
LIFE_PTS = {'Githzerai': 30, 'Rakshasa': 38, 'Illithid': 25, 'Tieflin': 35, 'Banshee': 28}
INTELLIGENCE_PTS = {'Githzerai': 15, 'Rakshasa': 10, 'Illithid': 25, 'Tieflin': 8, 'Banshee': 20}
STRENGTH_PTS = {'Githzerai': 12, 'Rakshasa': 20, 'Illithid': 10, 'Tieflin': 18, 'Banshee': 8}

# Constants used to set up player's experience gains and level
# XP_GAINS defines the experience (value) the player gets per enemy defeated, depending on the player's level (key)
# XP_LEVELS defines the experience (value) needed to obtain a new level(key)

XP_GAINS = {'1': 125, '2': 175, '3': 200, '4': 275, '5': 375, '6': 400, '7': 475, '8': 500, '9': 750}
XP_LEVELS = {'2': 500, '3': 1000, '4': 2000, '5': 3500, '6': 5000, '7': 7000, '8': 10000, '9': 15000, '10': 22000}

class Character:
    """
    Character is the base class for the player character and their enemies.
    Characters have a name, gender, race with special abilities and relating protection, intelligence, strength
    and life points.
    They can equip an armour, a spell and a weapon.
    """

    def __init__(self, name, gender, race, armour, weapon, spell, level=1):
        self.level = level
        self._name = name
        self._gender = gender
        self._race = race
        self.armour = armour
        self.weapon = weapon
        self.spell = spell
        if self._race == 'Githzerai':
            self._ability = ABILITIES['Githzerai']
            self.strength = STRENGTH_PTS['Githzerai']
            self.life = LIFE_PTS['Githzerai']
            self.intelligence = INTELLIGENCE_PTS['Githzerai']
        elif self._race == 'Rakshasa':
            self._ability = ABILITIES['Rakshasa']
            self.strength = STRENGTH_PTS['Rakshasa']
            self.life = LIFE_PTS['Rakshasa']
            self.intelligence = INTELLIGENCE_PTS['Rakshasa']
        elif self._race == 'Illithid':
            self._ability = ABILITIES['Illithid']
            self.strength = STRENGTH_PTS['Illithid']
            self.life = LIFE_PTS['Illithid']
            self.intelligence = INTELLIGENCE_PTS['Illithid']
        elif self._race == 'Tieflin':
            self._ability = ABILITIES['Tieflin']
            self.strength = STRENGTH_PTS['Tieflin']
            self.life = LIFE_PTS['Tieflin']
            self.intelligence = INTELLIGENCE_PTS['Tieflin']
        elif self._race == 'Banshee':
            self._ability = ABILITIES['Banshee']
            self.strength = STRENGTH_PTS['Banshee']
            self.life = LIFE_PTS['Banshee']
            self.intelligence = INTELLIGENCE_PTS['Banshee']

    def __repr__(self):
        return f"{self._name}, {self._gender}, {self._race}, ability : {self._ability['name']}, level : {self.level}" \
               f", armour : {self.armour}, life : {self.life}, strength : {self.strength}, intelligence : " \
               f"{self.intelligence}, weapon : {self.weapon}, spell : {self.spell}"

    def __str__(self):
        return f"Name : {self._name}\nGender : {self._gender}\nRace : {self._race}\nLevel : {self.level}\n" \
               f"Strength : {self.strength}\nIntelligence : {self.intelligence}\nLife : {self.life}\n" \
               f"Special Ability : {self._ability['name']}\n>>>>Equipment<<<<\n" \
               f"Armour : {self.armour.name} (protection : {self.armour.protection})\nWeapon : " \
               f"{self.weapon.name} (min.damage : {self.weapon.damage_min}, max. damage : {self.weapon.damage_max})\n" \
               f"Spell : {self.spell.name} (min.damage : {self.spell.damage_min}, max. damage : " \
               f"{self.spell.damage_max}\n"


class Player(Character):
    """Player has the same caracteristics as Character, with 3 more features.
    Inventory, containing armours, spells and protections, an amount of gold, and experience points.
    """

    def __init__(self, name, gender, race, armour, weapon, spell, level=1):
        Character.__init__(self, name, gender, race, armour, weapon, spell, level=1)
        self.inventory = []
        self.gold = random.randint(10, 200)
        self.experience = 0

    def __repr__(self):
        return Character.__repr__(self) + f", inventory : {self.inventory}, gold : {self.gold}"

    def __str__(self):
        return Character.__str__(self) + f">>>>Experience<<<<\n{self.experience} points. Next level in : " \
                                         f"{XP_LEVELS[str(self.level + 1)] - self.experience} points."

    def display_inventory(self):
        print(f">>>>{self._name}'s inventory<<<<")
        print(f"Gold : {self.gold}")
        for elt in self.inventory:
            if isinstance(elt, Weapon) or isinstance(elt, Spell):
                print(f"{elt.name} : min.damage : {elt.damage_min}, max. damage : {elt.damage_max}")
            elif isinstance(elt, Armour):
                print(f"{elt.name} : protection : {elt.protection}")


class Armour:
    """Armours are objects equiped by the player and their opponents.
    They have a name, a price, and some protection points that reduce damage (1 pp = -1 damage)
    Price is the amount of gold necessary to buy the armour at the shop.
    """

    def __init__(self, name, price, protection):
        self.name = name
        self.price = price
        self.protection = protection

    def __str__(self):
        return f"{self.name} : protection : {self.protection}, price : {self.price}"


class Weapon:
    """Weapons are objects equiped by the player and their opponents.
    They have a name, a price, a minimal damage and a maximal damage. Damage dealt by the weapon will therefore
    be bewteen min and max damage
    Price is the amount of gold necessary to buy the weapon at the shop.
    """

    def __init__(self, name, price, damage_min, damage_max):
        self.name = name
        self.price = price
        self.damage_min = damage_min
        self.damage_max = damage_max

    def __str__(self):
        return f"{self.name} : min. damage : {self.damage_min}, max. damage : {self.damage_max}, price : {self.price}"


class Spell(Weapon):
    """Spells are weapons too, but a player can equip them and desequip them during the fight, and so
    use multiple spells in the fight.
    In next version, there probably will be new features as such as : spells that don't deal damage but heal,
    spells that require mana points to be cast, etc
    """

    def __init__(self, name, price, damage_min, damage_max):
        Weapon.__init__(self, name, price, damage_min, damage_max)

    def __str__(self):
        return f"{self.name} : min. damage : {self.damage_min}, max. damage : {self.damage_max}, price : {self.price}"


class Shop:
    """A shop contains 3 inventories containing unlimited amount of weapons, spells and armours.
    The player can buy from these inventories if he has enough gold.
    The shop has only one instance, and its inventories are pre-initialized with 5 different armours, 5 different
    weapons and 5 different spells.
    """

    def __init__(self, stock_armour, stock_weapon, stock_spell):
        self.stock_armour = stock_armour
        self.stock_weapon = stock_weapon
        self.stock_spell = stock_spell

    def display(self, stock):
        """Displays the selected inventory : weapons or spells or armours' names, prices and damages."""
        for elt in stock:
            print(elt)

    def buy(self, item, player):
        """Checks if the player has enough gold to buy item and adds it to inventory while removing corresponding gold
        price or aborts operation."""
        if item.price > player.gold:
            print("You don't have enough gold to buy this piece of equipment.")
        else:
            player.inventory.append(item)
            player.gold -= item.price
            print(f"{item.name} added to inventory.")

    def sell(self, item, player):
        """Removes an item from player's inventory and adds to player's gold half of the item's price."""
        player.gold += item.price // 2
        player.inventory.remove(item)
        print(f"{item.name} sold for {item.price // 2} gold pieces.")
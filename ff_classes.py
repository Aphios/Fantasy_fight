"""Fantasy Fight Project

-- Version 0.1
Author : Sophie Blanchard
Purpose : simple fight game with fantasy characters
Start date : 03-17-2020
Last update : 03-19-2020

This file contains the classes :
- Character and its son Player
- Shop and its sons Weapon, Armour, Spell

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
PROTECTION_PTS = {'Githzerai': 5, 'Rakshasa': 10, 'Illithid': 3, 'Tieflin': 12, 'Banshee': 8}
LIFE_PTS = {'Githzerai': 30, 'Rakshasa': 38, 'Illithid': 25, 'Tieflin': 35, 'Banshee': 28}
INTELLIGENCE_PTS = {'Githzerai': 15, 'Rakshasa': 10, 'Illithid': 25, 'Tieflin': 8, 'Banshee': 20}
STRENGTH_PTS = {'Githzerai': 12, 'Rakshasa': 20, 'Illithid': 10, 'Tieflin': 18, 'Banshee': 8}

# Constants used to set up player's experience gains and level
# XP_GAINS defines the experience (value) the player gets per enemy defeated, depending on the player's level (key)
# XP_LEVELS defines the experience (value) needed to obtain a new level(key)

XP_GAINS = {'1': 125, '2': 175, '3': 200, '4': 275, '5': 375, '6': 400, '7': 475, '8': 500, '9': 750}
XP_LEVELS = {'2': 500, '3': 1000, '4': 2000, '5': 3500, '6': 5000, '7': 7000, '8': 10000, '9' : 15000, '10': 22000}

class Character:
    """
    Character is the base class for the player character and their enemies.
    Characters have a name, gender, race with special abilities and relating protection, intelligence, strength
    and life points.
    They can equip an armour, a spell and a weapon.
    """

    def __init__(self, name, gender, race, level=1, armour='underwear', weapon='fists', spell='None'):
        self.level = level
        self._name = name
        self._gender = gender
        self._race = race
        self.armour = armour
        self.weapon = weapon
        self.spell = spell
        if self._race == 'Githzerai':
            self._ability = ABILITIES['Githzerai']
            self.protection = PROTECTION_PTS['Githzerai']
            self.strength = STRENGTH_PTS['Githzerai']
            self.life = LIFE_PTS['Githzerai']
            self.intelligence = INTELLIGENCE_PTS['Githzerai']
        elif self._race == 'Rakshasa':
            self._ability = ABILITIES['Rakshasa']
            self.protection = PROTECTION_PTS['Rakshasa']
            self.strength = STRENGTH_PTS['Rakshasa']
            self.life = LIFE_PTS['Rakshasa']
            self.intelligence = INTELLIGENCE_PTS['Rakshasa']
        elif self._race == 'Illithid':
            self._ability = ABILITIES['Illithid']
            self.protection = PROTECTION_PTS['Illithid']
            self.strength = STRENGTH_PTS['Illithid']
            self.life = LIFE_PTS['Illithid']
            self.intelligence = INTELLIGENCE_PTS['Illithid']
        elif self._race == 'Tieflin':
            self._ability = ABILITIES['Tieflin']
            self.protection = PROTECTION_PTS['Tieflin']
            self.strength = STRENGTH_PTS['Tieflin']
            self.life = LIFE_PTS['Tieflin']
            self.intelligence = INTELLIGENCE_PTS['Tieflin']
        elif self._race == 'Banshee':
            self._ability = ABILITIES['Banshee']
            self.protection = PROTECTION_PTS['Banshee']
            self.strength = STRENGTH_PTS['Banshee']
            self.life = LIFE_PTS['Banshee']
            self.intelligence = INTELLIGENCE_PTS['Banshee']

    def __repr__(self):
        return f"{self._name}, {self._gender}, {self._race}, ability : {self._ability['name']}, level : {self.level}" \
               f", armour : {self.armour}, life : {self.life}, strength : {self.strength}, intelligence : " \
               f"{self.intelligence}, protection : {self.protection}, weapon : {self.weapon}, spell : " \
               f"{self.spell}"

    def __str__(self):
        return f"Name : {self._name}\nGender : {self._gender}\nRace : {self._race}\nLevel : {self.level}\n" \
               f"Strength : {self.strength}\nIntelligence : {self.intelligence}\nLife : {self.life}\n" \
               f"Protection : {self.protection}\nSpecial Ability : {self._ability['name']}\n>>>>Equipment<<<<\n" \
               f"Armour : {self.armour}\nWeapon : {self.weapon}\nSpell : {self.spell}\n"


class Player(Character):
    """Player has the same caracteristics as Character, with 3 more features.
    Inventory, containing armours, spells and protections, an amount of gold, and experience points.
    """

    def __init__(self, name, gender, race, level=1, armour='underwear', weapon='fists', spell='None'):
        Character.__init__(self, name, gender, race, level=1, armour='underwear', weapon='fists', spell='None')
        self.inventory = {}
        self.gold = random.randint(10, 200)
        self.experience = 0

    def __repr__(self):
        return Character.__repr__(self) + f", inventory : {self.inventory}, gold : {self.gold}"

    def __str__(self):
        return Character.__str__(self) + f">>>>Bag<<<<\nGold : {self.gold}\nInventory : {self.inventory}\n" \
                                         f">>>>Experience<<<<\n{self.experience} points. Next level in : " \
                                         f"{XP_LEVELS[str(self.level + 1)] - self.experience} points."


"""Fantasy Fight Project

-- Version 0.1
Author : Sophie Blanchard
Purpose : simple fight game with fantasy characters
Start date : 03-17-2020
Last update : 03-18-2020

This file contains the classes :
- Character and its son Player
- Shop and its sons Weapon, Armour, Spell

"""

class Character:
    """
    Character is the base class for the player character and their enemies.
    Characters have a name, gender, race with special abilities and relating protection, intelligence, strength
    and life points.
    They can equip an armour, a spell and a weapon.
    """

    ABILITIES: {'Githzerai': {'name': 'Vicious Swash', 'damage_min': -10, 'damage_max': 10},
                'Rakshasa': {'name': 'Subjugate', 'damage_min': -10, 'damage_max': 10},
                'Illithid': {'name': 'Mind pump', 'damage_min': -10, 'damage_max': 10},
                'Tieflin': {'name': 'Sting whip', 'damage_min': -10, 'damage_max': 10},
                'Banshee': {'name': 'Scream', 'damage_min': -10, 'damage_max': 10}}
    PROTECTION_PTS: {'Githzerai': 5, 'Rakshasa': 10, 'Illithid': 3, 'Tieflin': 12, 'Banshee': 8}
    LIFE_PTS: {'Githzerai': 30, 'Rakshasa': 38, 'Illithid': 25, 'Tieflin': 35, 'Banshee': 28}
    INTELLIGENCE_PTS: {'Githzerai': 15, 'Rakshasa': 10, 'Illithid': 25, 'Tieflin': 8, 'Banshee': 20}
    STRENGTH_PTS: {'Githzerai': 12, 'Rakshasa': 20, 'Illithid': 10, 'Tieflin': 18, 'Banshee': 8}

    def __init__(self, name, gender, race, level=1, armour='underwear', weapon='fists', spell='None'):
        self.level = level
        self.name = name
        self.gender = gender
        self.race = race
        self.armour = armour
        self.weapon = weapon
        self.spell = spell
        if self.race == 'Githzerai':
            self.ability = ABILITIES['Githzerai']
            self.protection = PROTECTION_PTS['Githzerai']
            self.strength = STRENGTH_PTS['Githzerai']
            self.life = LIFE_PTS['Githzerai']
            self.intelligence = INTELLIGENCE_PTS['Githzerai']
        elif self.race == 'Rakshasa':
            self.ability = ABILITIES['Rakshasa']
            self.protection = PROTECTION_PTS['Rakshasa']
            self.strength = STRENGTH_PTS['Rakshasa']
            self.life = LIFE_PTS['Rakshasa']
            self.intelligence = INTELLIGENCE_PTS['Rakshasa']
        elif self.race == 'Illithid':
            self.ability = ABILITIES['Illithid']
            self.protection = PROTECTION_PTS['Illithid']
            self.strength = STRENGTH_PTS['Illithid']
            self.life = LIFE_PTS['Illithid']
            self.intelligence = INTELLIGENCE_PTS['Illithid']
        elif self.race == 'Tieflin':
            self.ability = ABILITIES['Tieflin']
            self.protection = PROTECTION_PTS['Tieflin']
            self.strength = STRENGTH_PTS['Tieflin']
            self.life = LIFE_PTS['Tieflin']
            self.intelligence = INTELLIGENCE_PTS['Tieflin']
        elif self.race == 'Banshee':
            self.ability = ABILITIES['Banshee']
            self.protection = PROTECTION_PTS['Banshee']
            self.strength = STRENGTH_PTS['Banshee']
            self.life = LIFE_PTS['Banshee']
            self.intelligence = INTELLIGENCE_PTS['Banshee']

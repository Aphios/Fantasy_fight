"""Fantasy Fight Project

-- Version 0.1
Author : Sophie Blanchard
Purpose : simple fight game with fantasy characters
Start date : 03-17-2020
Last update : 04-01-2020

This file contains the classes :
- Character and its subclass Player
- Shop
- Weapon and its subclass Spell
- Armour

It also contains the constants needed to initialize class instances.

"""

import random
import pyinputplus as pyip
import functools

# Constants used to initialize characters

MALE_NAMES = ['Albert', 'Kronos', 'Alec', 'Bran', 'Urtuk', 'Shun']
FEMALE_NAMES = ['Lydia', 'Tulie', 'Aimee', 'Selene', 'Kira', 'Ksyncix']
OTHER_NAMES = ['Al', 'Effen', 'Juno', 'Lerrewen', 'Gorgo', 'Jviz']
GENDERS = ['Male', 'Female', 'Other']
RACES = ['Githzerai', 'Rakshasa', 'Illithid', 'Tieflin', 'Banshee']
ABILITIES = {'Githzerai': {'name': 'Vicious Swash', 'damage_min': -30, 'damage_max': 30},
             'Rakshasa': {'name': 'Subjugate', 'damage_min': -30, 'damage_max': 30},
             'Illithid': {'name': 'Mind pump', 'damage_min': -30, 'damage_max': 30},
             'Tieflin': {'name': 'Sting whip', 'damage_min': -30, 'damage_max': 30},
             'Banshee': {'name': 'Scream', 'damage_min': -30, 'damage_max': 30}}
LIFE_PTS = {'Githzerai': 30, 'Rakshasa': 38, 'Illithid': 25, 'Tieflin': 35, 'Banshee': 28}
INTELLIGENCE_PTS = {'Githzerai': 15, 'Rakshasa': 10, 'Illithid': 25, 'Tieflin': 8, 'Banshee': 20}
STRENGTH_PTS = {'Githzerai': 12, 'Rakshasa': 20, 'Illithid': 10, 'Tieflin': 18, 'Banshee': 8}

# Constants used to set up player's experience gains and level
# XP_GAINS defines the experience (value) the player gets per enemy defeated, depending on the enemy's level (key)
# XP_LEVELS defines the max experience (value) before reaching a new level(key), i.e. you are level 1 until 500,
# then level 2 from 501 to 1000, etc

XP_GAINS = {'1': 125, '2': 175, '3': 200, '4': 275, '5': 375, '6': 400, '7': 475, '8': 500, '9': 750}
XP_LEVELS = {'1': 500, '2': 1000, '3': 2000, '4': 3500, '5': 5000, '6': 7000, '7': 10000, '8': 15000, '9': 22000}


class Character:
    """
    Character is the base class for the player character and their enemies.
    Characters have a name, gender, race with special abilities and relating protection, intelligence, strength
    and life points.
    They can equip an armour, a spell and a weapon.
    """

    def __init__(self, name, gender, race, armour, weapon, spell, level=1):
        """Creates a character with a name, gender, race, weapon, spell and level.
        From race and level depends life, strength and intelligence.
        """
        self.level = level
        self._name = name
        self._gender = gender
        self._race = race
        self.armour = armour
        self.weapon = weapon
        self.spell = spell
        self.ability = ABILITIES[self._race]
        self.strength = STRENGTH_PTS[self._race]
        self.life = LIFE_PTS[self._race]
        self.intelligence = INTELLIGENCE_PTS[self._race]
        # Adjusting stats to character's level
        level_bonus_pts = functools.reduce(lambda a, b: a + (b // 2), range(self.level))
        self.ability.damage_min += level_bonus_pts
        self.ability.damage_max += level_bonus_pts
        self.life += level_bonus_pts
        self.strength += level_bonus_pts
        self.intelligence += level_bonus_pts

    def __repr__(self):
        return f"{self._name}, {self._gender}, {self._race}, ability : {self.ability['name']}, level : {self.level}" \
               f", armour : {self.armour}, life : {self.life}, strength : {self.strength}, intelligence : " \
               f"{self.intelligence}, weapon : {self.weapon}, spell : {self.spell}"

    def __str__(self):
        return f"Name : {self._name}\nGender : {self._gender}\nRace : {self._race}\nLevel : {self.level}\n" \
               f"Strength : {self.strength}\nIntelligence : {self.intelligence}\nLife : {self.life}\n" \
               f"Special Ability : {self.ability['name']}\n>>>>Equipment<<<<\n" \
               f"Armour : {self.armour.name} (protection : {self.armour.protection})\nWeapon : " \
               f"{self.weapon.name} (min.damage : {self.weapon.damage_min}, max. damage : {self.weapon.damage_max})\n" \
               f"Spell : {self.spell.name} (min.damage : {self.spell.damage_min}, max. damage : " \
               f"{self.spell.damage_max}\n"

    def random_attack(self):
        """Randomly returns a character's weapon, ability or spell (if existing) in order to attack."""
        if self.spell.name != 'No spell':
            return random.choice([self.weapon.name, self.spell.name, self.ability.name])
        else:
            return random.choice([self.weapon.name, self.ability.name])

    def hit(self, enemy, attack):
        """Dealts damage to enemy using attack, and prints a description of the attack."""
        if attack == self.weapon.name:
            damage = random.randint(self.weapon.damage_min, self.weapon.damage_max) + self.strength // 4
        elif attack == self.spell.name:
            damage = random.randint(self.spell.damage_min, self.spell.damage_max) + self.intelligence // 5
        else:
            damage = random.randint(self.ability.damage_min, self.ability.damage_max)

        final_damage = damage - enemy.armour.protection

        if final_damage > 0:
            enemy.life -= final_damage

        def desc_hit(damage, final_damage, enemy, attack):
            if final_damage > 0:
                return f"{self.name} uses {attack.lower()} to attack !\n{damage} damage points dealt !\n" \
                       f"{enemy.name}'s armour absorbs {damage - final_damage} damage points.\n" \
                       f"{enemy.name}'s life points are now {enemy.life}."
            else:
                return f"{self.name} uses {attack.lower()} to attack ! {enemy.name} dodges the attack!\n" \
                       f"{enemy.name}'s armour absorbs {damage - final_damage} damage points." \
                       f"{enemy.name}'s life points are still {enemy.life}."

        return desc_hit(damage, final_damage, enemy, attack)


class Player(Character):
    """Player has the same caracteristics as Character, with 3 more features.
    Inventory, containing armours, spells and protections, an amount of gold, and experience points.
    """

    def __init__(self, name, gender, race, armour, weapon, spell, level=1):
        Character.__init__(self, name, gender, race, armour, weapon, spell, level=1)
        self.inventory = []
        self.gold = random.randint(10, 200)
        self.experience = 0
        self.wins = 0

    def __repr__(self):
        return Character.__repr__(self) + f", inventory : {self.inventory}, gold : {self.gold}"

    def __str__(self):
        return Character.__str__(self) + f">>>>Experience<<<<\n{self.experience} points. Next level in : " \
                                         f"{XP_LEVELS[str(self.level)] - self.experience} points."

    def display_inventory(self):
        """Prints the players gold and inventory's content."""
        print(f">>>>{self._name}'s inventory<<<<")
        print(f"Gold : {self.gold}")
        for elt in self.inventory:
            if isinstance(elt, Weapon) or isinstance(elt, Spell):
                print(f"{elt.name} : min.damage : {elt.damage_min}, max. damage : {elt.damage_max}")
            elif isinstance(elt, Armour):
                print(f"{elt.name} : protection : {elt.protection}")

    def equip(self, item):
        """Updates player's armour or spell or weapon slot.
        The operation switches previous player's armour or spell or weapon with new one. Previous one is put in
        the player's inventory.
        """
        if isinstance(item, Weapon):
            self.inventory.append(self.weapon)
            self.weapon = item
        elif isinstance(item, Spell):
            self.inventory.append(self.spell)
            self.spell = item
        elif isinstance(item, Armour):
            self.inventory.append(self.armour)
            self.armour = item
        else:
            raise TypeError("Item's type must be Weapon, Spell or Armour")

    def loot(self):
        """Adds to player's gold a random amount of gold."""
        g = random.randint(0, 100)
        self.gold += g
        print(f"You looted {g} gold pieces.")

    def gain_xp(self, enemy):
        """Increases player's experience depending on enemy's level and levels player up if need be."""
        assert isinstance(enemy, Character)
        el = str(enemy.level)
        self.experience += XP_GAINS[el]
        print(f"You gain {XP_GAINS[el]} experience points.")
        while self.experience > XP_LEVELS[str(self.level)]:
            self.level_up()

    def level_up(self):
        """Increases player's level, life, strength, intelligence and special ability.
         Adds new player level // 2.
        """
        self.level += 1
        self.life += self.level // 2
        self.strength += self.level // 2
        self.intelligence += self.level // 2
        self.ability['damage_min'] += self.level // 2
        self.ability['damage_max'] += self.level // 2

        print(f"New level reached ! Congratulations, you are now level {self.level}.")

    def achievements(self):
        """Prints player's wins and level."""
        print(f">>>>> {self._name}'s achievements <<<<<\n{self.wins} enemies defeated. Last level reached : "
              f"{self.level}")

    def choose_attack(self):
        """Prompts the player to choose their weapon, ability or spell (if existing) to attack and returns choice."""
        if self.spell.name != 'No spell':
            print(f"Choose what you will use to attack :\nYour weapon : {self.weapon.name}, min.damage : "
                  f"{self.weapon.damage_min}, max.damage : {self.weapon.damage_max}\nYour special ability : "
                  f"{self.ability.name}, min. damage : {self.ability.damage_min}, max. damage : "
                  f"{self.ability.damage_max}\nYour spell : {self.spell.name}, min.damage : {self.spell.damage_min}, "
                  f"max.damage : {self.spell.damage_max}")
            choice = pyip.inputMenu([self.weapon.name, self.ability.name, self.spell.name], numbered=True)
        else:
            print(f"Choose what you will use to attack :\nYour weapon : {self.weapon.name}, min.damage : "
                  f"{self.weapon.damage_min}, max.damage : {self.weapon.damage_max}\nYour special ability : "
                  f"{self.ability.name}, min. damage : {self.ability.damage_min}, max. damage : "
                  f"{self.ability.damage_max}")
            choice = pyip.inputMenu([self.weapon.name, self.ability.name], numbered=True)
        return choice


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
        """Displays the equipment's stock passed as argument."""
        assert stock == self.stock_weapon or stock == self.stock_armour or stock == self.stock_spell
        """Displays the selected inventory : weapons or spells or armours' names, prices and damages."""
        for elt in stock:
            print(elt)

    def buy(self, item, player):
        """Checks if the player has enough gold to buy item and adds it to inventory while removing corresponding gold
        price or aborts operation."""
        assert isinstance(player, Player)
        assert isinstance(item, Weapon) or isinstance(item, Spell) or isinstance(item, Armour)
        if item.price > player.gold:
            print("You don't have enough gold to buy this piece of equipment.")
        else:
            player.inventory.append(item)
            player.gold -= item.price
            print(f"{item.name} added to inventory.")

    def sell(self, item, player):
        """Removes an item from player's inventory and adds to player's gold half of the item's price."""
        assert isinstance(player, Player)
        assert isinstance(item, Weapon) or isinstance(item, Spell) or isinstance(item, Armour)
        player.gold += item.price // 2
        player.inventory.remove(item)
        print(f"{item.name} sold for {item.price // 2} gold pieces.")

"""Fantasy Fight Project. A simple fight game with fantasy characters.

This file contains the classes :
- Character and its subclass Player
- Shop
- Weapon
- Spell
- Armour

It also contains the constants needed to initialize class instances.
"""

__version__ = 0.2
__author__ = "Sophie Blanchard"
__status__ = "Prototype"
__start_date__ = "03-17-2020"
__last_update__ = "04-17-2020"

import random
import pyinputplus as pyip
import functools

# Constants used to initialize characters

MALE_NAMES = ['Albert', 'Kronos', 'Alec', 'Bran', 'Urtuk', 'Shun']
FEMALE_NAMES = ['Lydia', 'Tulie', 'Aimee', 'Selene', 'Kira', 'Ksyncix']
OTHER_NAMES = ['Al', 'Effen', 'Juno', 'Lerrewen', 'Gorgo', 'Jviz']
GENDERS = ['Male', 'Female', 'Other']
RACES = ['Githzerai', 'Rakshasa', 'Illithid', 'Tieflin', 'Banshee']
ABILITIES = {'Githzerai': {'name': 'Vicious Swash', 'damage_min': -30, 'damage_max': 40},
             'Rakshasa': {'name': 'Subjugate', 'damage_min': -30, 'damage_max': 40},
             'Illithid': {'name': 'Mind pump', 'damage_min': -30, 'damage_max': 40},
             'Tieflin': {'name': 'Sting whip', 'damage_min': -30, 'damage_max': 40},
             'Banshee': {'name': 'Scream', 'damage_min': -30, 'damage_max': 40}}
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
        level_bonus_pts = functools.reduce(lambda a, b: a + (b // 2), range(self.level + 1))
        self.ability['damage_min'] += level_bonus_pts
        self.ability['damage_max'] += level_bonus_pts
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
            return random.choice([self.weapon.name, self.spell.name, self.ability['name']])
        else:
            return random.choice([self.weapon.name, self.ability['name']])

    def hit(self, enemy, attack):
        """Dealts damage to enemy using attack, and prints a description of the attack.

        Args :
        attack : the name (string) of weapon, spell or special ability used to hit
        enemy : a Character object.
        """
        if attack == self.weapon.name:
            dmg = random.randint(self.weapon.damage_min, self.weapon.damage_max) + self.strength // 4
        elif attack == self.spell.name:
            dmg = random.randint(self.spell.damage_min, self.spell.damage_max) + self.intelligence // 5
        else:
            dmg = random.randint(self.ability['damage_min'], self.ability['damage_max'])

        final_dmg = dmg - enemy.armour.protection

        if final_dmg > 0:
            enemy.life -= final_dmg

        self.desc_hit(dmg, final_dmg, enemy, attack)

    def desc_hit(self, damage, final_damage, enemy, attack):
        """Prints a description of the attack against the enemy.

        Args :
        enemy : a Character object
        attack : a string naming the attac
        damage and final_damage : ints
        """
        if final_damage > 0:
            print(f"{self._name} uses {attack.lower()} to attack !\n{damage} damage dealt !\n"
                  f"{enemy._name}'s armour absorbs {damage - final_damage} damage. \n"
                  f"{enemy._name}'s life points are now {enemy.life}.\n")
        else:
            print(f"{self._name} uses {attack.lower()} to attack ! {enemy._name} dodges the attack!\n"
                  f"{enemy._name}'s life points are still {enemy.life}.\n")


class Player(Character):
    """Player has the same caracteristics as Character, with 3 more features.

    Inventory, containing armours, spells and protections, an amount of gold, and experience points.
    """

    def __init__(self, name, gender, race, armour, weapon, spell):
        Character.__init__(self, name, gender, race, armour, weapon, spell, level=1)
        self.inventory = {}
        self.gold = random.randint(10, 200)
        self.experience = 0
        self.wins = 0

    def __repr__(self):
        return Character.__repr__(self) + f", inventory : {self.inventory}, gold : {self.gold}"

    def __str__(self):
        return Character.__str__(self) + f">>>>Experience<<<<\n{self.experience} points. Next level in : " \
                                         f"{XP_LEVELS[str(self.level)] - self.experience} points."

    def display_inventory(self):
        """Prints the player's gold and inventory's content."""
        print(f">>>>{self._name}'s inventory<<<<")
        print(f"Gold : {self.gold}")
        for elt in self.inventory.values():
            if isinstance(elt, Weapon) or isinstance(elt, Spell):
                print(f"{elt.name} : min.damage : {elt.damage_min}, max. damage : {elt.damage_max}")
            elif isinstance(elt, Armour):
                print(f"{elt.name} : protection : {elt.protection}")

    def equip(self, item):
        """Changes player's armour or spell or weapon.

        The operation switches previous player's armour or spell or weapon with new one. Previous one is put in
        the player's inventory, new one is removed from inventory.
        Args : item : the equipment's name
        Vars : eq : the object corresponding to the name item
        """
        eq = self.inventory[item]
        if isinstance(eq, Weapon):
            self.inventory[self.weapon.name] = self.weapon
            self.weapon = eq
        elif isinstance(eq, Spell):
            self.inventory[self.spell.name] = self.spell
            self.spell = eq
        elif isinstance(eq, Armour):
            self.inventory[self.armour.name] = self.armour
            self.armour = eq
        else:
            raise TypeError("Item's type must be Weapon, Spell or Armour")
        del self.inventory[item]

    def loot(self):
        """Adds to player's gold a random amount of gold."""
        g = random.randint(0, 100)
        self.gold += g
        print(f"You loot {g} gold pieces.")

    def gain_xp(self, enemy):
        """Increases player's experience depending on enemy's level and levels player up if need be."""
        assert isinstance(enemy, Character)
        el = str(enemy.level)
        self.experience += XP_GAINS[el]
        print(f"You gain {XP_GAINS[el]} experience points.")
        while self.experience > XP_LEVELS[str(self.level)]:
            self.level_up()

    def level_up(self):
        """Increases player's level, life, strength, intelligence and special ability."""
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
              f"{self.level}\n")

    def choose_attack(self):
        """Prompts the player to choose their weapon, ability or spell (if existing) to attack and returns choice."""
        if self.spell.name != 'No spell':
            print(f"Choose what you will use to attack :\nYour weapon : {self.weapon.name}, min.damage : "
                  f"{self.weapon.damage_min}, max.damage : {self.weapon.damage_max}\nYour special ability : "
                  f"{self.ability['name']}, min. damage : {self.ability['damage_min']}, max. damage : "
                  f"{self.ability['damage_max']}\nYour spell : {self.spell.name}, min.damage : "
                  f"{self.spell.damage_min}, max.damage : {self.spell.damage_max}\n")
            choice = pyip.inputMenu([self.weapon.name, self.ability['name'], self.spell.name], numbered=True)
        else:
            print(f"Choose what you will use to attack :\nYour weapon : {self.weapon.name}, min.damage : "
                  f"{self.weapon.damage_min}, max.damage : {self.weapon.damage_max}\nYour special ability : "
                  f"{self.ability['name']}, min. damage : {self.ability['damage_min']}, max. damage : "
                  f"{self.ability['damage_max']}\n")
            choice = pyip.inputMenu([self.weapon.name, self.ability['name']], numbered=True)
        return choice

    def available_items(self):
        """Returns the list of the items the player may sell or equip."""
        av_list = []
        for elt in self.inventory.values():
            if elt.price > 0:
                av_list.append(elt.name)
        if av_list:
            av_list.append('Nothing')
        return av_list

    def win_or_loose(self, enemy):
        """Returns true if the hero survives the fight (i.e. has at least 1 life point left), false otherwise."""
        if self.life > enemy.life:
            print("You win the fight !\n")
            return True
        elif self.life == enemy.life:
            print("You and your enemy die at each other's hands ! You mutually curse yourselves with your "
                  "last breath.\n")
        else:
            print("You lost the fight ! You are dead and now roam the realms of forgotten memories.\n")
        return False

    def buy(self, item, shop):
        """Buys an item from the shop and puts it in player's inventory.

        Checks if the player has enough gold to buy item and adds it to inventory while removing corresponding gold
        price, or aborts operation.
        Args : item : the string name of the object to buy
        Vars : eq : the corresponding object.
        """
        assert item in shop.stock
        eq = shop.stock[item]
        if eq.price > self.gold:
            print("You don't have enough gold to buy this piece of equipment.")
        else:
            self.inventory[item] = eq
            self.gold -= eq.price
            print(f"{item} added to inventory.")

    def sell(self, item):
        """Removes an item from player's inventory and adds to player's gold half of the item's price.

        Args : item : the string name of the object
        Vars : eq : the corresponding object.
        """
        assert item in self.inventory
        eq = self.inventory[item]
        self.gold += eq.price // 2
        del self.inventory[item]
        print(f"{item} sold for {eq.price // 2} gold pieces.")


class Armour:
    """Armours are objects equiped by the player and their opponents.

    They have a name, a price, and some protection points that reduce damage (1 pp = -1 damage)
    Price is the amount of gold necessary to buy the armour at the shop.
    """

    def __init__(self, name, price, protection):
        self.name = name
        self.price = price
        self.protection = protection
        self.nature = "Armour"

    def __str__(self):
        return f"{self.name} ({self.nature}) >> protection : {self.protection}, price : {self.price}"


class Weapon:
    """Weapons are objects equiped by the player and their opponents.

    They have a name, a price, a minimal damage and a maximal damage. Damage dealt by the weapon will therefore
    be between min and max damage
    Price is the amount of gold necessary to buy the weapon at the shop.
    """

    def __init__(self, name, price, damage_min, damage_max):
        self.name = name
        self.price = price
        self.damage_min = damage_min
        self.damage_max = damage_max
        self.nature = 'Weapon'

    def __str__(self):
        return f"{self.name} ({self.nature}) >> min. damage : {self.damage_min}, max. damage : {self.damage_max}, " \
               f"price : {self.price}"


class Spell():
    """Spells are objects equiped by the player and their opponents.

    In next version,the player will be able to equip them and desequip them during the fight, and so
    use multiple spells in the fight. There will be new features as such as : spells that don't deal damage but heal,
    spells that require mana points to be cast, etc...
    """

    def __init__(self, name, price, damage_min, damage_max):
        self.name = name
        self.price = price
        self.damage_min = damage_min
        self.damage_max = damage_max
        self.nature = 'Spell'

    def __str__(self):
        return f"{self.name} ({self.nature}) >> min. damage : {self.damage_min}, max. damage : {self.damage_max}, " \
               f"price : {self.price}"


class Shop:
    """A shop contains 3 inventories containing unlimited amount of weapons, spells and armours.

    The player can buy from these inventories if he has enough gold.
    The shop has only one instance, and its inventories are pre-initialized with 5 different armours, 5 different
    weapons and 5 different spells.
    """

    def __init__(self, stock):
        self.stock = stock
        self.list_sales = [elt for elt in stock]
        self.list_sales.append('Nothing')

    def display(self):
        """Displays the stocks."""
        for elt in self.stock.values():
            print(elt)

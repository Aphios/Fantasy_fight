"""Fantasy Fight Project. A simple fight game with fantasy characters.

This file contains the classes :
- Character and its subclass Player
"""

__version__ = 0.2
__author__ = "Sophie Blanchard"
__start_date__ = "03-17-2020"
__last_update__ = "05-02-2020"

import functools
import random
import pyinputplus as pyip
import pygame
import constants as cst
import items as it


pygame.init()


class Character:
    """Character is the base class for the player character and their enemies.

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
        self.ability = cst.ABILITIES[self._race]
        self.strength = cst.STRENGTH_PTS[self._race]
        self.life = cst.LIFE_PTS[self._race]
        self.intelligence = cst.INTELLIGENCE_PTS[self._race]
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

        return self.desc_hit(dmg, final_dmg, enemy, attack)

    def desc_hit(self, damage, final_damage, enemy, attack):
        """Prints a description of the attack against the enemy.

        Args :
        enemy : a Character object
        attack : a string naming the attac
        damage and final_damage : ints
        """
        if final_damage > 0:
            return f"{self._name} uses {attack.lower()} to attack !\n{damage} damage dealt !\n"\
                   f"{enemy._name}'s armour absorbs {damage - final_damage} damage. \n"\
                   f"{enemy._name}'s life points are now {enemy.life}.\n"
        else:
            return f"{self._name} uses {attack.lower()} to attack ! {enemy._name} dodges the attack !\n"\
                   f"{enemy._name}'s life points are still {enemy.life}.\n"


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
        return Character.__str__(self) + f">>>>Experience<<<<\n{self.experience} points. Next level in : "\
                                         f"{cst.XP_LEVELS[str(self.level)] - self.experience} points.\n" + self.display_inventory()

    def display_inventory(self):
        """Prints the player's gold and inventory's content."""
        inv = ""
        for elt in self.inventory.values():
            if isinstance(elt, it.Weapon) or isinstance(elt, it.Spell):
                inv += f"{elt.name} : min.damage : {elt.damage_min}, max. damage : {elt.damage_max}\n"
            elif isinstance(elt, it.Armour):
                inv += f"{elt.name} : protection : {elt.protection}\n"
        return f">>>>{self._name}'s inventory<<<<\nGold : {self.gold}\n" + inv


    def equip(self, item):
        """Changes player's armour or spell or weapon.

        The operation switches previous player's armour or spell or weapon with new one. Previous one is put in
        the player's inventory, new one is removed from inventory.
        Args : item : the equipment's name
        Vars : eq : the object corresponding to the name item
        """
        eq = self.inventory[item]
        if isinstance(eq, it.Weapon):
            self.inventory[self.weapon.name] = self.weapon
            self.weapon = eq
        elif isinstance(eq, it.Spell):
            self.inventory[self.spell.name] = self.spell
            self.spell = eq
        elif isinstance(eq, it.Armour):
            self.inventory[self.armour.name] = self.armour
            self.armour = eq
        else:
            raise TypeError("Item's type must be Weapon, Spell or Armour")
        del self.inventory[item]

    def loot(self):
        """Adds to player's gold a random amount of gold."""
        g = random.randint(0, 100)
        self.gold += g
        return f"You loot {g} gold pieces."

    def gain_xp(self, enemy):
        """Increases player's experience depending on enemy's level and levels player up if need be."""
        assert isinstance(enemy, Character)
        el = str(enemy.level)
        self.experience += cst.XP_GAINS[el]
        return f"You gain {cst.XP_GAINS[el]} experience points."

    def level_up(self):
        """Increases player's level, life, strength, intelligence and special ability."""
        self.level += 1
        self.life += self.level // 2
        self.strength += self.level // 2
        self.intelligence += self.level // 2
        self.ability['damage_min'] += self.level // 2
        self.ability['damage_max'] += self.level // 2

        return f"New level reached ! Congratulations, you are now level {self.level}."

    def achievements(self):
        """Prints player's wins and level."""
        return f">>>>> {self._name}'s achievements <<<<<\n{self.wins} enemies defeated. Last level reached : " \
               f"{self.level}\n"

    def choose_attack(self):
        """Prompts the player to choose their weapon, ability or spell (if existing) to attack."""
        if self.spell.name != 'No spell':
            return f"Please write down the name of the attack you wish to launch against" \
                   f" your enemy.\nYour weapon : {self.weapon.name}, min.damage : "\
                   f"{self.weapon.damage_min}, max.damage : {self.weapon.damage_max}\nYour special ability : "\
                   f"{self.ability['name']}, min. damage : {self.ability['damage_min']}, max. damage : "\
                   f"{self.ability['damage_max']}\nYour spell : {self.spell.name}, min.damage : "\
                   f"{self.spell.damage_min}, max.damage : {self.spell.damage_max}\n"
        else:
            return f"Please write down the name of the attack you wish to launch against" \
                   f" your enemy.\nYour weapon : {self.weapon.name}, min.damage : "\
                   f"{self.weapon.damage_min}, max.damage : {self.weapon.damage_max}\nYour special ability : "\
                   f"{self.ability['name']}, min. damage : {self.ability['damage_min']}, max. damage : "\
                   f"{self.ability['damage_max']}\n"

    def available_attacks(self):
        """Returns a list of the names the player may use in combat."""
        res = [self.weapon.name, self.ability['name']]
        if self.spell.name != 'No spell':
            res.append(self.spell.name)
        return res

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
        """Returns description of how hero survives the fight or fell."""
        if self.life > enemy.life:
            return "You win the fight !\n"
        elif self.life == enemy.life:
            return "You and your enemy die at each other's hands ! You mutually curse yourselves with your "\
                  "last breath.\n"
        else:
            return "You lost the fight ! You are dead and now roam the realms of forgotten memories.\n"

    def buy(self, item, shop):
        """Buys an item from the shop and puts it in player's inventory.

        Checks if the player has enough gold to buy item and adds it to inventory while removing corresponding gold
        price, or aborts operation.
        Args : item : the string name of the object to buy
        Vars : eq : the corresponding object.
        """
        assert item in shop.stock_armour or item in shop.stock_weapon or item in shop.stock_spell
        if item in shop.stock_weapon:
            eq = shop.stock_weapon[item]
        elif item in shop.stock_armour:
            eq = shop.stock_armour[item]
        elif item in shop.stock_spell:
            eq = shop.stock_spell[item]
        if eq.price > self.gold:
            return "You don't have enough gold to buy this piece of equipment."
        else:
            self.inventory[item] = eq
            self.gold -= eq.price
            return f"{item} added to inventory."

    def sell(self, item):
        """Removes an item from player's inventory and adds to player's gold half of the item's price.

        Args : item : the string name of the object
        Vars : eq : the corresponding object.
        """
        assert item in self.inventory
        eq = self.inventory[item]
        self.gold += eq.price // 2
        del self.inventory[item]
        return f"{item} sold for {eq.price // 2} gold pieces."

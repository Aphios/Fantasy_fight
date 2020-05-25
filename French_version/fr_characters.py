"""Fantasy Fight Project. A simple fight game with fantasy characters.

This file contains the classes :
- Character and its subclass Player
"""

__version__ = 0.3
__author__ = "Sophie Blanchard"
__start_date__ = "03-17-2020"
__last_update__ = "05-17-2020"

import functools
import random

import pygame

import French_version.fr_constants as cst
import French_version.fr_items as it


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
        self.name = name
        self.gender = gender
        self.race = race
        self.armour = armour
        self.weapon = weapon
        self.spell = spell
        self.ability = cst.ABILITIES[self.race]
        self.strength = cst.STRENGTH_PTS[self.race]
        self.life = cst.LIFE_PTS[self.race]
        self.intelligence = cst.INTELLIGENCE_PTS[self.race]
        # GUI attributes
        self.pic = cst.PICTURES[self.race][self.gender]
        self.hit_sound = pygame.mixer.Sound("Sound/hit.wav")
        self.spell_sound = pygame.mixer.Sound("Sound/spell.wav")
        self.gold_sound = pygame.mixer.Sound("Sound/coins.wav")
        self.equip_sound = pygame.mixer.Sound("Sound/bag.wav")
        self.win_sound = pygame.mixer.Sound("Sound/win.wav")
        self.loose_sound = pygame.mixer.Sound("Sound/loose.wav")
        # Adjusting stats to character's level
        level_bonus_pts = functools.reduce(lambda a, b: a + (b // 2), range(self.level + 1))
        self.ability['dommages_mini'] += level_bonus_pts
        self.ability['dommages_maxi'] += level_bonus_pts
        self.life += level_bonus_pts
        self.strength += level_bonus_pts
        self.intelligence += level_bonus_pts

    def __repr__(self):
        return f"{self.name}, {self.gender}, {self.race}, pouvoir : {self.ability['nom']}, niveau : {self.level}" \
               f", armure : {self.armour}, vie : {self.life}, force : {self.strength}, intelligence : " \
                   f"{self.intelligence}, arme : {self.weapon}, sort : {self.spell}"

    def __str__(self):
        return f"Nom : {self.name}\nGenre : {self.gender}\nRace : {self.race}\nNiveau : {self.level}\n" \
               f"Force : {self.strength}\nIntelligence : {self.intelligence}\nVie : {self.life}\n" \
               f"Pouvoir : {self.ability['nom']}\n>>>>Equipement<<<<\n" \
               f"Armure : {self.armour.name} (protection : {self.armour.protection})\nArme : " \
               f"{self.weapon.name} (dommages mini : {self.weapon.damage_min}, dommages maxi : {self.weapon.damage_max})\n" \
               f"Sort : {self.spell.name} (dommages mini : {self.spell.damage_min}, dommages maxi : " \
               f"{self.spell.damage_max})\n"

    def random_attack(self):
        """Randomly returns a character's weapon, ability or spell (if existing) in order to attack."""
        if self.spell.name != 'Aucun sort':
            return random.choice([self.weapon.name, self.spell.name, self.ability['nom']])
        else:
            return random.choice([self.weapon.name, self.ability['nom']])

    def hit(self, enemy, attack):
        """Dealts damage to enemy using attack, and retunrs a description of the attack.

        Args :
        attack : the name (string) of weapon, spell or special ability used to hit
        enemy : a Character object.
        Plays a spell or hit sound with pygame.
        """
        if attack == self.weapon.name:
            dmg = random.randint(self.weapon.damage_min, self.weapon.damage_max) + self.strength // 4
            self.hit_sound.play()
        elif attack == self.spell.name:
            dmg = random.randint(self.spell.damage_min, self.spell.damage_max) + self.intelligence // 5
            self.spell_sound.play()
        else:
            dmg = random.randint(self.ability['dommages_mini'], self.ability['dommages_maxi'])
            self.spell_sound.play()

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
            return f"{self.name} utilise {attack.lower()} pour attaquer !\n{damage} dommages !\n"\
                   f"L'armure de {enemy.name} absorbe {damage - final_damage} dommages. \n"\
                   f"Les points de vie de {enemy.name} sont désormais à {enemy.life}.\n"
        else:
            return f"{self.name} utilise {attack.lower()} pour attaquer ! {enemy.name} esquive l'attaque !\n"\
                   f"Les points de vie de {enemy.name} sont toujours à {enemy.life}.\n"


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
        return Character.__repr__(self) + f", inventaire : {self.inventory}, pièces d'or : {self.gold}"

    def __str__(self):
        return Character.__str__(self) + f">>>>Expérience<<<<\n{self.experience} points. Prochain niveau dans : "\
                                         f"{cst.XP_LEVELS[str(self.level)] - self.experience} points.\n" + self.display_inventory()

    def display_inventory(self):
        """Prints the player's gold and inventory's content."""
        inv = ""
        for elt in self.inventory.values():
            if isinstance(elt, it.Weapon) or isinstance(elt, it.Spell):
                inv += f"{elt.name} : dommages mini : {elt.damage_min}, dommages maxi : {elt.damage_max}\n"
            elif isinstance(elt, it.Armour):
                inv += f"{elt.name} : protection : {elt.protection}\n"
        return f">>>>Inventaire de {self.name}<<<<\nPièces d'or : {self.gold}\n" + inv


    def equip(self, item):
        """Changes player's armour or spell or weapon.

        The operation switches previous player's armour or spell or weapon with new one. Previous one is put in
        the player's inventory, new one is removed from inventory.
        Args : item : the equipment's name
        Vars : eq : the object corresponding to the name item
        Plays equip sound in pygame.
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
        self.equip_sound.play()

    def loot(self):
        """Adds to player's gold a random amount of gold."""
        g = random.randint(2, 100)
        self.gold += g
        self.gold_sound.play()
        return f"Vous récupérez {g} pièces d'or."

    def gain_xp(self, enemy):
        """Increases player's experience depending on enemy's level and levels player up if need be."""
        assert isinstance(enemy, Character)
        el = str(enemy.level)
        self.experience += cst.XP_GAINS[el]
        return f"Vous gagnez {cst.XP_GAINS[el]} points d'expérience."

    def level_up(self):
        """Increases player's level, life, strength, intelligence and special ability."""
        self.level += 1
        self.life += self.level // 2
        self.strength += self.level // 2
        self.intelligence += self.level // 2
        self.ability['dommages_mini'] += self.level // 2
        self.ability['dommages_maxi'] += self.level // 2
        self.win_sound.play()
        return f"Félicitations, vous avez atteint le niveau {self.level} !"

    def achievements(self):
        """Prints player's wins and level."""
        return f">>>>> Succès de {self.name} <<<<<\n{self.wins} ennemi(s) éliminé(s). Dernier niveau atteint : " \
               f"{self.level}\n"

    def choose_attack(self):
        """Prompts the player to choose their weapon, ability or spell (if existing) to attack."""
        if self.spell.name != 'Aucun sort':
            return f"Ecrivez ci-dessous le nom de l'attaque que vous souhaitez lancer contre votre ennemi." \
                   f" Votre arme : {self.weapon.name}, dommages mini : "\
                   f"{self.weapon.damage_min}, dommages maxi : {self.weapon.damage_max}\nVotre pouvoir : "\
                   f"{self.ability['nom']}, dommages mini : {self.ability['dommages_mini']}, dommages maxi : "\
                   f"{self.ability['dommages_maxi']}\nVotre sort : {self.spell.name}, dommages mini : "\
                   f"{self.spell.damage_min}, dommages maxi : {self.spell.damage_max}\n"
        else:
            return f"Ecrivez ci-dessous le nom de l'attaque que vous souhaitez lancer contre votre ennemi." \
                   f" Votre arme : {self.weapon.name}, dommages mini : " \
                   f"{self.weapon.damage_min}, dommages maxi : {self.weapon.damage_max}\nVotre pouvoir : " \
                   f"{self.ability['nom']}, dommages mini : {self.ability['dommages_mini']}, dommages maxi : " \
                   f"{self.ability['dommages_maxi']}\n"

    def available_attacks(self):
        """Returns a list of the names the player may use in combat."""
        res = [self.weapon.name, self.ability['nom']]
        if self.spell.name != 'Aucun sort':
            res.append(self.spell.name)
        return res

    def available_items(self):
        """Returns the list of the items the player may sell or equip."""
        av_list = []
        for elt in self.inventory.values():
            if elt.price > 0:
                av_list.append(elt.name)
        if av_list:
            av_list.append('Rien')
        return av_list

    def win_or_loose(self, enemy):
        """Returns description of how hero survives the fight or fell."""
        if self.life > enemy.life:
            self.win_sound.play()
            return "Vous remportez le combat !\n"
        elif self.life == enemy.life:
            self.loose_sound.play()
            return "Vous et votre ennemi décédez sous vos coups mutuels ! Vous vous maudissez tous deux dans votre "\
                  "dernier souffle.\n"
        else:
            self.loose_sound.play()
            return "Vous avez perdu le combat ! Vous êtes mort et hantez le royaume des héros oubliés.\n"

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
            self.gold_sound.play()
            return "Vous n'avez pas assez d'or pour acheter\ncette pièce d'équipement."
        else:
            self.inventory[item] = eq
            self.gold -= eq.price
            self.equip_sound.play()
            return f"Transaction réussie !\nL'objet est disponible dans votre inventaire."

    def sell(self, item):
        """Removes an item from player's inventory and adds to player's gold half of the item's price.

        Args : item : the string name of the object
        Vars : eq : the corresponding object.
        """
        assert item in self.inventory
        eq = self.inventory[item]
        self.gold += eq.price // 2
        del self.inventory[item]
        self.gold_sound.play()
        return f"Transaction réussie ! Equipement vendu pour {eq.price // 2} pièces d'or."

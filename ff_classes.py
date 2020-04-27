"""Fantasy Fight Project. A simple fight game with fantasy characters.

This file contains the classes :
- Character and its subclass Player
- Shop
- Weapon
- Spell
- Armour
- Button
- GameScene and its subclasses
"""

__version__ = 0.2
__author__ = "Sophie Blanchard"
__status__ = "Prototype"
__start_date__ = "03-17-2020"
__last_update__ = "04-27-2020"

import random
import pyinputplus as pyip
import functools
import ff_constants as ffc
import pygame
import time

pygame.init()

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
        self.ability = ffc.ABILITIES[self._race]
        self.strength = ffc.STRENGTH_PTS[self._race]
        self.life = ffc.LIFE_PTS[self._race]
        self.intelligence = ffc.INTELLIGENCE_PTS[self._race]
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
                  f"{enemy._name}'s life points are now {enemy.life}.")
        else:
            print(f"{self._name} uses {attack.lower()} to attack ! {enemy._name} dodges the attack!\n"
                  f"{enemy._name}'s life points are still {enemy.life}.")


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
                                         f"{ffc.XP_LEVELS[str(self.level)] - self.experience} points."

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
        self.experience += ffc.XP_GAINS[el]
        print(f"You gain {ffc.XP_GAINS[el]} experience points.")
        while self.experience > ffc.XP_LEVELS[str(self.level)]:
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
              f"{self.level}")

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
        assert item in shop.stock_armour or item in shop.stock_weapon or item in shop.stock_spell
        if item in shop.stock_weapon:
            eq = shop.stock_weapon[item]
        elif item in shop.stock_armour:
            eq = shop.stock_armour[item]
        elif item in shop.stock_spell:
            eq = shop.stock_spell[item]
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

    def __init__(self, armours, spells, weapons):
        self.stock_armour = armours
        self.stock_spell = spells
        self.stock_weapon = weapons
        self.list_armour_sales = [elt for elt in armours]
        self.list_armour_sales.append('Nothing')
        self.list_spell_sales = [elt for elt in spells]
        self.list_spell_sales.append('Nothing')
        self.list_weapon_sales = [elt for elt in weapons]
        self.list_weapon_sales.append('Nothing')

    def display_armour(self):
        """Displays the armour stocks."""
        for elt in self.stock_armour.values():
            print(elt)

    def display_weapon(self):
        """Displays the weapon stocks."""
        for elt in self.stock_weapon.values():
            print(elt)

    def display_spell(self):
        """Displays the spell stocks."""
        for elt in self.stock_spell.values():
            print(elt)


# GUI classes
class Button:
    """A button with a text."""

    def __init__(self, text, text_color, bg_color, font):
        self.msg = font.render(text, True, text_color, bg_color)
        self.box = self.msg.get_rect()

    def blit_button(self, surf, center):
        """Blits the button onto the Surface at coordinates x, y."""
        self.box.center = center
        surf.blit(self.msg, self.box)


# Game states classes
class Game:
    """A master-class to contain each game scene (just as in theater scenes)."""

    def __init__(self):
        self.window = pygame.display.set_mode(ffc.RESOLUTION)
        self.continue_button = Button('Continue', ffc.BLACK, ffc.BURGUNDY, ffc.IMMORTAL_BIG)
        self.clock = pygame.time.Clock()
        self.logo = pygame.image.load('Images/FF_logo.png').convert_alpha()
        pygame.display.set_caption("Fantasy Fight")
        pygame.display.set_icon(self.logo)

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

    def blit_text(self, text, position, font, color):
        """Blits hashed text in the window, respecting newlines.

        Args : position : a tuple / font : font object / color : color object / text : string
        / surface : surface object.
        Rendering is anti-aliased.
        """
        words = [word.split(' ') for word in text.splitlines()]
        space = font.size(' ')[0]  # The width of a space.
        max_width, max_height = self.window.get_size()
        x, y = position
        for line in words:
            for word in line:
                word_surface = font.render(word, True, color)
                word_width, word_height = word_surface.get_size()
                if x + word_width >= max_width:
                    x = position[0]  # Reset the x.
                    y += word_height  # Start on new row.
                self.window.blit(word_surface, (x, y))
                x += word_width + space
            x = position[0]  # Reset the x.
            y += word_height  # Start on new row.

    def text_buttons(self, color_surf, font, color_font, text, pos_text, button_1, pos_button_1,
                     button_2=None, pos_button_2=None):
        """Blits texts on a colored Surface, with one or two buttons."""
        self.window.fill(color_surf)
        self.blit_text(text, pos_text, font, color_font)
        button_1.blit_button(self.window, pos_button_1)
        if button_2:
            button_2.blit_button(self.window, pos_button_2)
        pygame.display.flip()


class GameTitle(Game):
    """First game scene + music.

     The introduction screen with the game's title.
     """

    def update(self):
        """Loads intro music and Plays intro music and renders intro screen"""
        pygame.mixer_music.set_volume(0.50)
        pygame.mixer_music.load("Music/the-descent.mp3")
        pygame.mixer_music.play(-1)
        intro_screen = pygame.image.load('Images/Fantasy_fight.png').convert_alpha()
        self.window.blit(intro_screen, (0, 0))
        self.blit_text("Fantasy Fight\n", (280, 270), ffc.IMMORTAL_BIG, ffc.BLACK)
        pygame.display.flip()
        time.sleep(2)


class GameStory(Game):
    """Displays the story of the game."""

    def update(self):
        self.text_buttons(ffc.VIOLET, ffc.IMMORTAL_SMALL, ffc.BLACK, "Fantasy Fight is a basic "
                          "'read and choose' game.\n~~~STORY~~~\nYou enter the Forgotten Realms, a fantasy world "
                          "where heroes fight for power and glory.\n~~~GOAL~~~\nYour goal is to defeat as many "
                          "enemies as you can and gain eternal renoun !", (10, 50), self.continue_button, (400, 500))


class GameRules(Game):
    """Displays the game rules."""

    def update(self):
        self.text_buttons(ffc.VIOLET, ffc.IMMORTAL_SMALL, ffc.BLACK, "~~~RULES~~~\nYou will create a "
                          "character and be given some money (or not if you're unlucky !) to buy some "
                          "equipment.\nYou can choose to be a Rakshasa, an Illithid, a Tieflin, a Banshee or a "
                          "Githzerai.\nFrom your race depends your life force, your strength, your intelligence and "
                          "your special ability.\nYou will be able to buy weapons, armours and spells. You can also "
                          "sell equipment in your inventory.\nYou cannot sell your current weapon, spell or armour "
                          "unless you equip something else.\nThen you will fight other characters "
                          "until you die or choose to retire.\nEach enemy defeated is rewarded by experience points "
                          "and a chance to loot some gold.\nWhen you have earned enough experience, you will gain a "
                          "level and your stats will increase.\n", (10, 50), frame.continue_button, (400, 500))


class GameTips(Game):
    """Displays the game tips."""

    def update(self):
        self.text_buttons(ffc.VIOLET, ffc.IMMORTAL_SMALL, ffc.BLACK, "~~~Fighting tips~~~\nBefore "
                          "entering a fight, know that :\n- you may cause damage to your enemy with your "
                          "weapon (the more strong you are, the more damage you do),\n with your spell (the more clever"
                          "you are, the more damage you do),\n or with your ability (this one is tricky : it can make "
                          "a lot of damage but has also a more important fail risk.)\n- there is always a chance "
                          "that your blow (or your adversary's) might fail.\n~~~Ending game~~~\nYou may quit the "
                          "game at any time.\nCaution ! This game does NOT save your character or your stats. It is"
                          " a one-shot game !\nGood luck, and have fun !", (10, 50), frame.continue_button, (400, 500))


class GameOver(Game):
    """Displays the game over message and credits."""

    def update(self):
        self.blit_text("~~~Game over~~~\nThank you for playing !\n~~~CREDITS~~~\nConception & "
                       "programming : Aphios\nMusic:\n'The Descent' by Kevin MacLeod\nLink: "
                       "https://incompetech.filmmusic.io/song/4490-the-descent\nLicense: "
                       "http://creativecommons.org/licenses/by/4.0/\n'Crossing the Chasm' by Kevin MacLeod\n"
                       "Link: https://incompetech.filmmusic.io/song/3562-crossing-the-chasm\nLicense: "
                       "http://creativecommons.org/licenses/by/4.0/\n'Killers' by Kevin MacLeod\n"
                       "Link: https://incompetech.filmmusic.io/song/3952-killers\nLicense: "
                       "http://creativecommons.org/licenses/by/4.0/\n'The Path of the Goblin King' by Kevin MacLeod"
                       "Link: https://incompetech.filmmusic.io/song/4503-the-path-of-the-goblin-king\nLicense: "
                       "http://creativecommons.org/licenses/by/4.0/\n", (10, 500), ffc.IMMORTAL_SMALL, ffc.BLACK)
        time.sleep(20)


class Pause(Game):
    """Freezes the game until the continue button is hit."""

    def handle_events(self):
        pause = True
        while pause:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
                if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                    if frame.continue_button.box.collidepoint(event.pos):
                        return


class Yes_No(Game):
    """Freezes the game until the YES or the NO button is hit."""

    def handle_events(self):
        GameScene.handle_events()
        # TODO hit button 1 or button 2

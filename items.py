"""Fantasy Fight Project. A simple fight game with fantasy characters.

This file contains the classes :
- Shop
- Weapon
- Spell
- Armour
"""

__version__ = 0.2
__author__ = "Sophie Blanchard"
__status__ = "Prototype"
__start_date__ = "03-17-2020"
__last_update__ = "04-28-2020"


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
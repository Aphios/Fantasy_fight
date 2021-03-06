"""Fantasy Fight Project. A simple fight game with fantasy characters.

This file contains the classes :
- Shop
- Weapon
- Spell
- Armour
"""

__version__ = 0.2
__author__ = "Sophie Blanchard"
__start_date__ = "03-17-2020"
__last_update__ = "05-17-2020"


class Armour:
    """Armours are objects equiped by the player and their opponents.

    They have a name, a price, and some protection points that reduce damage (1 pp = -1 damage)
    Price is the amount of gold necessary to buy the armour at the shop.
    """

    def __init__(self, name, price, protection):
        self.name = name
        self.price = price
        self.protection = protection
        self.nature = "Armure"

    def __str__(self):
        return f"{self.name} ({self.nature}) >> protection : {self.protection}, prix : {self.price}\n"


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
        self.nature = 'Arme'

    def __str__(self):
        return f"{self.name} ({self.nature}) >> dommages mini : {self.damage_min}, dommages maxi : {self.damage_max}, " \
               f"prix : {self.price}\n"


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
        self.nature = 'Sort'

    def __str__(self):
        return f"{self.name} ({self.nature}) >> dommages mini : {self.damage_min}, dommages maxi : {self.damage_max}, " \
               f"prix : {self.price}\n"


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
        self.list_armour_sales.append('Rien')
        self.list_spell_sales = [elt for elt in spells]
        self.list_spell_sales.append('Rien')
        self.list_weapon_sales = [elt for elt in weapons]
        self.list_weapon_sales.append('Rien')

    def display_armour(self):
        """Displays the armour stocks."""
        a_stock = ''
        for elt in self.stock_armour.values():
            a_stock += str(elt)
        return a_stock

    def display_weapon(self):
        """Displays the weapon stocks."""
        w_stock = ''
        for elt in self.stock_weapon.values():
            w_stock += str(elt)
        return w_stock

    def display_spell(self):
        """Displays the spell stocks."""
        s_stock = ''
        for elt in self.stock_spell.values():
            s_stock += str(elt)
        return s_stock


# ITEMS CREATION
corset = Armour('Corset', 100, 4)
leathersuit = Armour('Combinaison en cuir', 250, 8)
rags = Armour('Haillons', 10, 1)
underwear = Armour('Sous-vêtements', 0, 0)
platemail = Armour('Armure de plates', 700, 12)
mithril_jacket = Armour('Veste en mithril', 1500, 22)
blizzard = Spell('Blizzard', 200, 11, 20)
scorch = Spell('Etincelle', 100, 6, 13)
venom_gaze = Spell('Poison', 150, 8, 18)
wasp_stings = Spell('Piqûre', 50, 0, 8)
lightning = Spell('Eclair', 400, 24, 33)
no_spell = Spell('Aucun sort', 0, 0, 0)
scythe = Weapon('Faux', 400, 24, 33)
scissors = Weapon('Ciseaux', 50, 0, 8)
katana = Weapon('Katana', 200, 11, 20)
club = Weapon('Gourdin', 100, 6, 13)
dagger = Weapon('Dague', 150, 8, 18)
fists = Weapon('Poings', 0, -2, 6)

# Inventories and shop creation
stock_armour = {'Corset': corset, 'Combinaison en cuir': leathersuit, 'Haillons': rags, 'Armure de plates': platemail,
                'Veste en mithril': mithril_jacket}
stock_weapon = {'Faux': scythe, 'Ciseaux': scissors,'Katana': katana, 'Gourdin': club, 'Dague': dagger}
stock_spell = {'Blizzard': blizzard, 'Etincelle': scorch, 'Poison': venom_gaze, 'Piqûre': wasp_stings,
               'Eclair': lightning}
shop = Shop(stock_armour, stock_spell, stock_weapon)
"""Fantasy Fight Project

-- Version 0.1
Author : Sophie Blanchard
Purpose : simple fight game with fantasy characters
Start date : 03-17-2020
Last update : 03-26-2020

This file is used to test parts of the program or elements in the sub files.
"""
import ff_classes as ffc
import random

# Main functions copied here fot the sake of tests

def autogen(genders, races, male_names, female_names, other_names, armours, weapons, spells):
    """Generates random settings for a character.
    The function returns a name, a gender a race, a weapon, an armour and a spell.
    """
    gender = random.choice(genders)
    race = random.choice(races)
    if gender == 'Male':
        name = random.choice(male_names)
    elif gender == 'Female':
        name = random.choice(female_names)
    else:
        name = random.choice(other_names)
    armour = random.choice(armours)
    weapon = random.choice(weapons)
    spell = random.choice(spells)
    return {'name' : name, 'gender' : gender, 'race' : race, 'armour' : armour, 'weapon' : weapon, 'spell' : spell}


# Equipment creation
corset = ffc.Armour('Corset', 100, 5)
leathersuit = ffc.Armour('Leathersuit', 250, 10)
rags = ffc.Armour('Rags', 10, 1)
underwear = ffc.Armour('Underwear', 0, 0)
platemail = ffc.Armour('Platemail', 700, 25)
mithril_jacket = ffc.Armour('Mithril jacket', 1500, 40)
blizzard = ffc.Spell('Blizzard', 200, 8, 16)
scorch = ffc.Spell('Scorch', 100, 4, 10)
venom_gaze = ffc.Spell('Venom gaze', 150, 15, 25)
wasp_stings = ffc.Spell('Wasp stings', 50, -5, 6)
lightning = ffc.Spell('Lightning', 400, 25, 35)
no_spell = ffc.Spell('No spell', 0, 0, 0)
scythe = ffc.Weapon('Scythe', 400, 25, 35)
scissors = ffc.Weapon('Scissors', 50, -5, 6)
halbert = ffc.Weapon('Halbert', 200, 8, 16)
club = ffc.Weapon('Club', 100, 4, 10)
dagger = ffc.Weapon('Dagger', 150, 15, 25)
fists = ffc.Weapon('Fists', 0, -8, 4)

# Equipment access to attribute
print('SCYTHE price, max and min :', scythe.price, scythe.damage_max, scythe.damage_min)
print('WASP_STINGS : ', wasp_stings)
rags.price += 50
rags.protection = 10
print('RAGS (price +50, prot 10) : ', rags)

# Inventories creation
armours = {corset, leathersuit, rags, platemail, mithril_jacket}
spells = {blizzard, scorch, venom_gaze, wasp_stings, lightning}
weapons = {scythe, scissors, halbert, club, dagger}

# Shop creation
shop = ffc.Shop(armours, weapons, spells)

# Shop display
print('DISPLAY SHOP SPELLS')
shop.display(shop.stock_spell)

# Player initialization and attribute access
aphios = ffc.Player('Aphios', 'other', 'Banshee', underwear, fists, no_spell)
print('PLAYER APHIOS : ', aphios)
aphios.wins += 2
print('APHIOS WINS : ', aphios.wins)
aphios.armour = platemail
aphios.life -= 5
print('APHIOS with life -5 and platemail : ', aphios)

# Player inventory display
print('Display APHIOS INVENTORY')
aphios.display_inventory()

# Player loot
aphios.loot()
print('APHIOS GOLD AFTER LOOT : ', aphios.gold)

# Enemy creation and attribute access
settings = autogen(ffc.GENDERS, ffc.RACES, ffc.MALE_NAMES, ffc.FEMALE_NAMES, ffc.OTHER_NAMES, [corset, rags, leathersuit],
                   [scissors, fists, dagger], [scorch, wasp_stings, no_spell])
enemy = ffc.Character(**settings)
print('ENEMY :', enemy)
enemy.strength += 2
enemy.life = 23
enemy.spell = lightning
print('ENEMY after strength +2, life 23 with lightning', enemy)

# Buy and sell
aphios.gold = 200
shop.buy(scissors, aphios)
print('APHIOS INVENTORY WITH NEW SCISSORS')
aphios.display_inventory()
shop.sell(scissors, aphios)
print('APHIOS INVENTORY AFTER SELLING SCISSORS')
aphios.display_inventory()

# XP gain and levelup, achievements
aphios.experience = 200
boss = ffc.Character('Boss', 'Other', 'Tieflin', platemail, club, no_spell, 5)
aphios.gain_xp(boss)
aphios.wins += 1
print('APHIOS XP after defeating level 5 boss : ', aphios.experience)
print('APHIOS NEW STATS : ', aphios)
aphios.achievements()
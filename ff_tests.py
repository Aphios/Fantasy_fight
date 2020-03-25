"""Fantasy Fight Project

-- Version 0.1
Author : Sophie Blanchard
Purpose : simple fight game with fantasy characters
Start date : 03-17-2020
Last update : 03-24-2020

This file is used to test parts of the program or elements in the sub files.
"""
import ff_classes as ffc
import random

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


# Test Shop creation and display

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

# Inventories creation
armours = {corset, leathersuit, rags, platemail, mithril_jacket}
spells = {blizzard, scorch, venom_gaze, wasp_stings, lightning}
weapons = {scythe, scissors, halbert, club, dagger}

# Shop creation
shop = ffc.Shop(armours, weapons, spells)

# Player initialization, buy and sell
aphios = ffc.Player('Aphios', 'other', 'Banshee', underwear, fists, no_spell)
print(aphios.wins)
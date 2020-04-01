"""Fantasy Fight Project

-- Version 0.1
Author : Sophie Blanchard
Purpose : simple fight game with fantasy characters
Start date : 03-17-2020
Last update : 04-01-2020

This file is used to test the main program's functions.
Tests to be runned with Pytest.
"""

import ff_classes as ffc
import random

# Test values
males = {'Bob', 'Alex'}
females = {'Sam', 'Alice'}
others = {'Tic', 'Tac'}
corset = ffc.Armour('Corset', 100, 5)
underwear = ffc.Armour('Underwear', 0, 0)
blizzard = ffc.Spell('Blizzard', 200, 8, 16)
no_spell = ffc.Spell('No spell', 0, 0, 0)
dagger = ffc.Weapon('Dagger', 150, 15, 25)
fists = ffc.Weapon('Fists', 0, -8, 4)
genders = ['Male', 'Female', 'Unknown']

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

# AUTOGEN
# Assert it returns a dict
# Assert it returns correct values
# Test incorrect parameter : race
# Test incorrect parameter : gender
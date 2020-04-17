"""Fantasy Fight Project. A  simple fight game with fantasy characters.

This file is used to test the main program's functions.
Tests to be runned with Pytest.
"""

__version__ = 0.2
__author__ = "Sophie Blanchard"
__status__ = "Prototype"
__start_date__ = "03-17-2020"
__last_update__ = "04-17-2020"

import ff_classes as ffc
import random

# Test values
males = ['Bob', 'Alex']
females = ['Sam', 'Alice']
others = ['Tic', 'Tac']
corset = ffc.Armour('Corset', 100, 5)
underwear = ffc.Armour('Underwear', 0, 0)
blizzard = ffc.Spell('Blizzard', 200, 8, 16)
no_spell = ffc.Spell('No spell', 0, 0, 0)
dagger = ffc.Weapon('Dagger', 150, 15, 25)
fists = ffc.Weapon('Fists', 0, -8, 4)
genders = ['Male', 'Female', 'Unknown']
races = ['Elf', 'Gobelin', 'Dwarf']

def autogen(genders, races, male_names, female_names, other_names, armours, weapons, spells):
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
def test_autogen_returns_dict():
    assert isinstance(autogen(genders, races, males, females, others, [corset, underwear], [dagger, fists],
                   [blizzard, no_spell]), dict)


def test_autogen_length():
    assert len(autogen(genders, races, males, females, others, [corset, underwear], [dagger, fists],
                   [blizzard, no_spell])) == 6


def test_autogen_strings():
    r = autogen(genders, races, males, females, others, [corset, underwear], [dagger, fists],
                   [blizzard, no_spell])
    assert isinstance(r['name'], str)


def test_autogen_objects():
    r = autogen(genders, races, males, females, others, [corset, underwear], [dagger, fists],
                [blizzard, no_spell])
    assert isinstance(r['weapon'], ffc.Weapon)




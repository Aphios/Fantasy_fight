"""Fantasy Fight Project. A  simple fight game with fantasy characters.

This file is used to test the main program's functions.
Tests to be runned with Pytest.
"""

__version__ = 0.2
__author__ = "Sophie Blanchard"
__status__ = "Prototype"
__start_date__ = "03-17-2020"
__last_update__ = "05-06-2020"


import items
import func

# Test values
males = ['Bob', 'Alex']
females = ['Sam', 'Alice']
others = ['Tic', 'Tac']
corset = items.Armour('Corset', 100, 5)
underwear = items.Armour('Underwear', 0, 0)
blizzard = items.Spell('Blizzard', 200, 8, 16)
no_spell = items.Spell('No spell', 0, 0, 0)
dagger = items.Weapon('Dagger', 150, 15, 25)
fists = items.Weapon('Fists', 0, -8, 4)
genders = ['Male', 'Female', 'Unknown']
races = ['Elf', 'Gobelin', 'Dwarf']


# AUTOGEN
def test_autogen_returns_dict():
    assert isinstance(func.autogen(genders, races, males, females, others, [corset, underwear], [dagger, fists],
                   [blizzard, no_spell]), dict)


def test_autogen_length():
    assert len(func.autogen(genders, races, males, females, others, [corset, underwear], [dagger, fists],
                   [blizzard, no_spell])) == 6


def test_autogen_strings():
    r = func.autogen(genders, races, males, females, others, [corset, underwear], [dagger, fists],
                   [blizzard, no_spell])
    assert isinstance(r['name'], str)


def test_autogen_objects():
    r = func.autogen(genders, races, males, females, others, [corset, underwear], [dagger, fists],
                [blizzard, no_spell])
    assert isinstance(r['weapon'], items.Weapon)




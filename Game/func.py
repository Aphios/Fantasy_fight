"""Fantasy Fight Project. A  simple fight game with fantasy characters.

This file contains the main game functions.
"""

__version__ = 0.2
__author__ = "Sophie Blanchard"
__start_date__ = "03-17-2020"
__last_update__ = "05-04-2020"

import random
import time

import pygame

import constants

pygame.init()


def autogen(genders, races, male_names, female_names, other_names, armours, weapons, spells):
    """Generates random settings for a character.

    Returns : a dict containing a name, a gender, a race, a weapon, an armour and a spell.
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
    return {'name': name, 'gender': gender, 'race': race, 'armour': armour, 'weapon': weapon, 'spell': spell}









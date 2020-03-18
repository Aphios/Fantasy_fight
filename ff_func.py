"""Fantasy Fight Project

-- Version 0.1
Author : Sophie Blanchard
Purpose : simple fight game with fantasy characters
Start date : 03-17-2020
Last update : 03-18-2020

This file contains the functions used in the main program.
"""

import random
import ff_constants as cst

def autogen():
    """Generates random settings for a character.
    The function returns a name, a gender and a race randomly selected from set constants in ff_constants.
    """
    gender = random.choice(cst.GENDERS)
    race = random.choice(cst.RACES)
    if gender == 'Male':
        name = random.choice(cst.MALE_NAMES)
    elif gender == 'Female':
        name = random.choice(cst.FEMALE_NAMES)
    else:
        name = random.choice(cst.OTHER_NAMES)
    return {'name' : name, 'gender' : gender, 'race' : race}
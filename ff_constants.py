"""Fantasy Fight Project. A simple fight game with fantasy characters.

This file contains the constants needed to initialize class instances.
"""

__version__ = 0.2
__author__ = "Sophie Blanchard"
__status__ = "Prototype"
__start_date__ = "03-17-2020"
__last_update__ = "04-27-2020"


import pygame

pygame.font.init()

# Constants used to initialize characters

MALE_NAMES = ['Albert', 'Kronos', 'Alec', 'Bran', 'Urtuk', 'Shun']
FEMALE_NAMES = ['Lydia', 'Tulie', 'Aimee', 'Selene', 'Kira', 'Ksyncix']
OTHER_NAMES = ['Al', 'Effen', 'Juno', 'Lerrewen', 'Gorgo', 'Jviz']
GENDERS = ['Male', 'Female', 'Other']
RACES = ['Githzerai', 'Rakshasa', 'Illithid', 'Tieflin', 'Banshee']
ABILITIES = {'Githzerai': {'name': 'Vicious Swash', 'damage_min': -30, 'damage_max': 40},
             'Rakshasa': {'name': 'Subjugate', 'damage_min': -30, 'damage_max': 40},
             'Illithid': {'name': 'Mind pump', 'damage_min': -30, 'damage_max': 40},
             'Tieflin': {'name': 'Sting whip', 'damage_min': -30, 'damage_max': 40},
             'Banshee': {'name': 'Scream', 'damage_min': -30, 'damage_max': 40}}
LIFE_PTS = {'Githzerai': 30, 'Rakshasa': 38, 'Illithid': 25, 'Tieflin': 35, 'Banshee': 28}
INTELLIGENCE_PTS = {'Githzerai': 15, 'Rakshasa': 10, 'Illithid': 25, 'Tieflin': 8, 'Banshee': 20}
STRENGTH_PTS = {'Githzerai': 12, 'Rakshasa': 20, 'Illithid': 10, 'Tieflin': 18, 'Banshee': 8}

# Constants used to set up player's experience gains and level
# XP_GAINS defines the experience (value) the player gets per enemy defeated, depending on the enemy's level (key)
# XP_LEVELS defines the max experience (value) before reaching a new level(key), i.e. you are level 1 until 500,
# then level 2 from 501 to 1000, etc

XP_GAINS = {'1': 125, '2': 175, '3': 200, '4': 275, '5': 375, '6': 400, '7': 475, '8': 500, '9': 750}
XP_LEVELS = {'1': 500, '2': 1000, '3': 2000, '4': 3500, '5': 5000, '6': 7000, '7': 10000, '8': 15000, '9': 22000}

# Pygame Constants
RESOLUTION = (800, 600)

# Colors
VIOLET = (108, 73, 179)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREY = (105, 95, 110)
NAVY = (7, 53, 179)
BURGUNDY = (122, 15, 36)

# Fonts
IMMORTAL_BIG = pygame.font.Font('Fonts/immortal.ttf', 36)
IMMORTAL_SMALL = pygame.font.Font('Fonts/immortal.ttf', 16)

# Animation
FPS = 30
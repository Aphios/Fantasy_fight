"""Fantasy Fight Project. A simple fight game with fantasy characters.

This file contains the constants needed to initialize class instances.
"""

__version__ = 0.2
__author__ = "Sophie Blanchard"
__start_date__ = "03-17-2020"
__last_update__ = "05-17-2020"


import pygame

pygame.font.init()

# Constants used to initialize characters

MALE_NAMES = ['Albert', 'Kronos', 'Alec', 'Bran', 'Urtuk', 'Shun']
FEMALE_NAMES = ['Lydia', 'Tulie', 'Aimee', 'Selene', 'Kira', 'Ksyncix']
OTHER_NAMES = ['Al', 'Effen', 'Juno', 'Lerrewen', 'Gorgo', 'Jviz']
GENDERS = ['Homme', 'Femme', 'Autre']
RACES = ['Githzerai', 'Rakshasa', 'Illithid', 'Tieflin', 'Banshee']
ABILITIES = {'Githzerai': {'nom': 'Déferlement', 'dommages_mini': -30, 'dommages_maxi': 40},
             'Rakshasa': {'nom': 'Envoûtement', 'dommages_mini': -30, 'dommages_maxi': 40},
             'Illithid': {'nom': 'Décervelation', 'dommages_mini': -30, 'dommages_maxi': 40},
             'Tieflin': {'nom': 'Fouet', 'dommages_mini': -30, 'dommages_maxi': 40},
             'Banshee': {'nom': 'Hurlement', 'dommages_mini': -30, 'dommages_maxi': 40}}
LIFE_PTS = {'Githzerai': 30, 'Rakshasa': 38, 'Illithid': 25, 'Tieflin': 35, 'Banshee': 28}
INTELLIGENCE_PTS = {'Githzerai': 15, 'Rakshasa': 10, 'Illithid': 25, 'Tieflin': 8, 'Banshee': 20}
STRENGTH_PTS = {'Githzerai': 12, 'Rakshasa': 20, 'Illithid': 10, 'Tieflin': 18, 'Banshee': 8}

# Constants used to set up player's experience gains and level
# XP_GAINS defines the experience (value) the player gets per enemy defeated, depending on the enemy's level (key)
# XP_LEVELS defines the max experience (value) before reaching a new level(key), i.e. you are level 1 until 500,
# then level 2 from 501 to 1000, etc

XP_GAINS = {'1': 10, '2': 50, '3': 50, '4': 100, '5': 200, '6': 200, '7': 500, '8': 500, '9': 1000}
XP_LEVELS = {'1': 20, '2': 100, '3': 200, '4': 350, '5': 500, '6': 700, '7': 1500, '8': 2500, '9': 4500, '10': 8000}

# Pygame Constants
RESOLUTION = (800, 600)

# Colors
VIOLET = (108, 73, 179)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
PRUNE_GREY = (105, 95, 110)
NAVY = (7, 53, 179)
BURGUNDY = (122, 15, 36)
GOLD = (237, 206, 31)
GREY = (166, 166, 166)

# Fonts
IMMORTAL_BIG = pygame.font.Font('Fonts/immortal.ttf', 36)
IMMORTAL_SMALL = pygame.font.Font('Fonts/immortal.ttf', 18)

# Animation
FPS = 30

# Character pictures
PICTURES = {'Githzerai':
                {'Homme': 'Images/githzeraiM.png', 'Femme': 'Images/githzeraiF.png','Autre': 'Images/githzeraiO.png'},
            'Rakshasa':
                {'Homme': 'Images/RakshasaM.png', 'Femme': 'Images/RakshasaF.png', 'Autre': 'Images/RakshasaO.png'},
            'Illithid':
                {'Homme': 'Images/IllithidM.png', 'Femme': 'Images/IllithidF.png', 'Autre': 'Images/IllithidO.png'},
            'Tieflin':
                {'Homme': 'Images/tieflinM.png', 'Femme': 'Images/tieflinF.png', 'Autre': 'Images/tieflinO.png'},
            'Banshee':
                {'Homme': 'Images/BansheeM.png', 'Femme': 'Images/BansheeF.png', 'Autre': 'Images/BansheeO.png'}}
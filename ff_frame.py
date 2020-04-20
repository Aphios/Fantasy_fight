"""Fantasy Fight Project. A simple fight game with fantasy characters.

This file contains the base GUI frame made with pygame.
"""

__version__ = 0.2
__author__ = "Sophie Blanchard"
__status__ = "Prototype"
__start_date__ = "03-17-2020"
__last_update__ = "04-20-2020"


import pygame
import time
import random
import pyinputplus as pyip
import ff_classes as ffc
import ff_main as ffm

pygame.init()

# CONSTANTS
RESOLUTION = (800, 600)

# Colors
VIOLET = (108, 73, 179)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREY = (105, 95, 110)
NAVY = (7, 53, 179)
BURGUNDY = (122, 15, 36)

#Fonts
immortal_big = pygame.font.Font('Fonts/immortal.ttf', 24)
immortal_small = pygame.font.Font('Fonts/immortal.ttf', 16)

# Animation
FPS = 30

# GAME ELEMENTS
# Window creation
window = pygame.display.set_mode(RESOLUTION)

# Clock creation
clock = pygame.time.Clock()

# Images
intro_screen = pygame.image.load('Images/Fantasy_fight.png').convert_alpha()
logo = pygame.image.load('Images/FF_logo.png').convert_alpha()

# Personnalize window
pygame.display.set_caption("Fantasy Fight")
pygame.display.set_icon(logo)

# Individual equipment creation
corset = ffc.Armour('Corset', 100, 4)
leathersuit = ffc.Armour('Leathersuit', 250, 8)
rags = ffc.Armour('Rags', 10, 1)
underwear = ffc.Armour('Underwear', 0, 0)
platemail = ffc.Armour('Platemail', 700, 12)
mithril_jacket = ffc.Armour('Mithril jacket', 1500, 22)
blizzard = ffc.Spell('Blizzard', 200, 11, 20)
scorch = ffc.Spell('Scorch', 100, 6, 13)
venom_gaze = ffc.Spell('Venom gaze', 150, 8, 18)
wasp_stings = ffc.Spell('Wasp stings', 50, 0, 8)
lightning = ffc.Spell('Lightning', 400, 24, 33)
no_spell = ffc.Spell('No spell', 0, 0, 0)
scythe = ffc.Weapon('Scythe', 400, 24, 33)
scissors = ffc.Weapon('Scissors', 50, 0, 8)
halbert = ffc.Weapon('Halbert', 200, 11, 20)
club = ffc.Weapon('Club', 100, 6, 13)
dagger = ffc.Weapon('Dagger', 150, 8, 18)
fists = ffc.Weapon('Fists', 0, -2, 6)

# Inventories and shop creation
stocks = {'Corset': corset, 'Leathersuit': leathersuit, 'Rags': rags, 'Platemail': platemail,
          'Mithril jacket': mithril_jacket, 'Blizzard': blizzard, 'Scorch': scorch, 'Venom gaze': venom_gaze,
          'Wasp stings': wasp_stings, 'Lightning': lightning, 'Scythe': scythe, 'Scissors': scissors,
          'Halbert': halbert, 'Club': club, 'Dagger': dagger}
shop = ffc.Shop(stocks)

# >>>>>> *** GAME LOOP *** <<<<<<<<
launched = True

while launched:

    # GAME INTRO
    # Play intro music
    pygame.mixer_music.set_volume(0.50)
    pygame.mixer_music.load("Music/the-descent.mp3")
    pygame.mixer_music.play(-1)
    # Intro screen
    window.blit(intro_screen, (0, 0))
    ffm.blit_text(window, ffm.title, (240, 270), immortal_big, BLACK)
    pygame.display.flip()
    time.sleep(2)
    # Intro text
    window.fill(VIOLET)
    ffm.blit_text(window, ffm.story, (10, 50), immortal_small, BLACK)
    pygame.display.flip()
    time.sleep(3)
    ffm.blit_text(window, ffm.rules, (10, 160), immortal_small, BLACK)
    pygame.display.flip()
    # TODO : Replace sleep() by next button ; executes remaining program
    time.sleep(3)
    window.fill(VIOLET)
    pygame.display.flip()
    ffm.blit_text(window, ffm.tips, (10, 10), immortal_small, BLACK)
    pygame.display.flip()
    time.sleep(3)
    # Stop intro music
    pygame.mixer_music.fadeout(2500)

    # Shop and equip phases (play 'The path of the goblin king')

    # Fight phase (play randomly 'Killers' or 'Crossing the chasm')

    # End game (play 'The descent')

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            launched = False

    pygame.display.flip()
    clock.tick(FPS)
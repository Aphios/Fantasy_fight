"""Fantasy Fight Project. A simple fight game with fantasy characters.

This file contains the main game loop.
"""

__version__ = 0.2
__author__ = "Sophie Blanchard"
__status__ = "Prototype"
__start_date__ = "03-17-2020"
__last_update__ = "04-29-2020"


import pygame
import time
import constants
import characters as char
import items
import scenes
import func
import gui_elements as gui


pygame.init()

# Game creation
fantasy_fight = scenes.Game()

# Individual equipment creation
corset = items.Armour('Corset', 100, 4)
leathersuit = items.Armour('Leathersuit', 250, 8)
rags = items.Armour('Rags', 10, 1)
underwear = items.Armour('Underwear', 0, 0)
platemail = items.Armour('Platemail', 700, 12)
mithril_jacket = items.Armour('Mithril jacket', 1500, 22)
blizzard = items.Spell('Blizzard', 200, 11, 20)
scorch = items.Spell('Scorch', 100, 6, 13)
venom_gaze = items.Spell('Venom gaze', 150, 8, 18)
wasp_stings = items.Spell('Wasp stings', 50, 0, 8)
lightning = items.Spell('Lightning', 400, 24, 33)
no_spell = items.Spell('No spell', 0, 0, 0)
scythe = items.Weapon('Scythe', 400, 24, 33)
scissors = items.Weapon('Scissors', 50, 0, 8)
halbert = items.Weapon('Halbert', 200, 11, 20)
club = items.Weapon('Club', 100, 6, 13)
dagger = items.Weapon('Dagger', 150, 8, 18)
fists = items.Weapon('Fists', 0, -2, 6)

# Inventories and shop creation
stock_armour = {'Corset': corset, 'Leathersuit': leathersuit, 'Rags': rags, 'Platemail': platemail,
                'Mithril jacket': mithril_jacket}
stock_weapon = {'Scythe': scythe, 'Scissors': scissors,'Halbert': halbert, 'Club': club, 'Dagger': dagger}
stock_spell = {'Blizzard': blizzard, 'Scorch': scorch, 'Venom gaze': venom_gaze, 'Wasp stings': wasp_stings,
               'Lightning': lightning}
shop = items.Shop(stock_armour, stock_spell, stock_weapon)

# Scenes creation and ordering
# GAME INTRO
title = scenes.GameTitle()
story = scenes.GameStory()
rules = scenes.GameRules()
tips = scenes.GameTips()
pause = scenes.Pause()
intro_queue = [title, story, pause, rules, pause, tips, pause]
# CHARACTER CREATION
naming = scenes.EnterName()
genring = scenes.EnterGender()
racing = scenes.EnterRace()
# ENDING
end = scenes.GameOver()

# >>>>>> *** GAME LOOP *** <<<<<<<<
launched = True

while launched:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

    # STORY DISPLAY
    for scene in intro_queue :
        scene.handle_events()
        scene.run()
        fantasy_fight.clock.tick(constants.FPS)

    # CHARACTER CREATION
    # Player's name
    naming.handle_events()
    p_name = naming.run()
    fantasy_fight.clock.tick(constants.FPS)
    # Player's gender
    p_gender = ''
    while not func.verify_ui(p_gender, constants.GENDERS):
        genring.handle_events()
        p_gender = genring.run()
        fantasy_fight.clock.tick(constants.FPS)
    # Player's race
    p_race = ''
    while not func.verify_ui(p_race, constants.RACES):
        racing.handle_events()
        p_race = genring.run()
        fantasy_fight.clock.tick(constants.FPS)

    print(p_race)




        # Stop intro music when shoping or fighting starts
        #pygame.mixer_music.fadeout(2500)

    # Shop and equip phases (play 'The path of the goblin king')

    # Fight phase (play randomly 'Killers' or 'Crossing the chasm')

    # End game (play 'The descent')

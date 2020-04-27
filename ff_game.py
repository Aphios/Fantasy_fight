"""Fantasy Fight Project. A simple fight game with fantasy characters.

This file contains the base GUI frame made with pygame.
"""

__version__ = 0.2
__author__ = "Sophie Blanchard"
__status__ = "Prototype"
__start_date__ = "03-17-2020"
__last_update__ = "04-27-2020"


import pygame
import ff_constants as cst
import ff_classes as ffc


pygame.init()

fantasy_fight = ffc.Game()

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
stock_armour = {'Corset': corset, 'Leathersuit': leathersuit, 'Rags': rags, 'Platemail': platemail,
                'Mithril jacket': mithril_jacket}
stock_weapon = {'Scythe': scythe, 'Scissors': scissors,'Halbert': halbert, 'Club': club, 'Dagger': dagger}
stock_spell = {'Blizzard': blizzard, 'Scorch': scorch, 'Venom gaze': venom_gaze, 'Wasp stings': wasp_stings,
               'Lightning': lightning}
shop = ffc.Shop(stock_armour, stock_spell, stock_weapon)


# >>>>>> *** GAME LOOP *** <<<<<<<<
launched = True

while launched:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            launched = False

        # GAME INTRO
    title = ffc.GameTitle()
    story = ffc.GameStory()
    rules = ffc.GameRules()
    tips = ffc.GameTips()
    pause = ffc.Pause()
    intro_queue = [title, story, pause, rules, pause, tips]
    for scene in intro_queue :
        scene.handle_events()
        scene.update()
        fantasy_fight.clock.tick(cst.FPS)


        # Stop intro music
        #pygame.mixer_music.fadeout(2500)

        # Shop and equip phases (play 'The path of the goblin king')

        # Fight phase (play randomly 'Killers' or 'Crossing the chasm')

        # End game (play 'The descent')

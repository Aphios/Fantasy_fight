"""Fantasy Fight Project. A simple fight game with fantasy characters.

This file contains the main game loop.
"""

__version__ = 0.2
__author__ = "Sophie Blanchard"
__status__ = "Prototype"
__start_date__ = "03-17-2020"
__last_update__ = "05-01-2020"


import pygame
import time
import constants
import characters as char
import game_states as states
import items
import scenes as scn
import func
import gui_elements as gui


pygame.init()

# Initialize game
game = states.Game()

# >>>>>> *** GAME LOOP *** <<<<<<<<
launched = True

while launched:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

    # INTRO
    scn.title.handle_events()
    scn.title.play_music(-1)
    game.window.blit(game.screen, (0, 0))
    scn.title.display_text((280, 270), game.font_big)
    time.sleep(3)
    game.clock.tick(constants.FPS)

    # STORY DISPLAY
    # Display story
    scn.story.handle_events()
    game.window.blit(game.bg, (0, 0))
    scn.story.display_text_continue()
    game.clock.tick(constants.FPS)
    # Pause before displaying rules
    scn.pause.handle_events()
    scn.rules.handle_events()
    game.window.blit(game.bg, (0, 0))
    scn.rules.display_text_continue()
    game.clock.tick(constants.FPS)
    # Pause before displaying tips
    scn.pause.handle_events()
    scn.tips.handle_events()
    game.window.blit(game.bg, (0, 0))
    scn.tips.display_text_continue()
    game.clock.tick(constants.FPS)
    # Pause before entering player creation
    scn.pause.handle_events()

    # PLAYER CREATION
    # Player's name
    scn.enter_name.handle_events()
    game.window.blit(game.bg, (0, 0))
    scn.enter_name.ask_user()
    p_name = game.get_ui()
    # Player's gender
    game.input_box.clear()
    p_gender = ''
    while not func.verify_ui(p_gender, constants.GENDERS):
        scn.enter_gender.handle_events()
        game.window.blit(game.bg, (0, 0))
        scn.enter_gender.ask_user()
        p_gender = game.get_ui()
    # Player's race
    game.input_box.clear()
    p_race = ''
    while not func.verify_ui(p_race, constants.RACES):
        scn.enter_race.handle_events()
        game.window.blit(game.bg, (0, 0))
        scn.enter_race.ask_user()
        p_race = game.get_ui()
    # Register player as a game attribute
    game.player = char.Player(p_name, p_gender, p_race, items.underwear, items.fists, items.no_spell)

    # WELCOME PLAYER
    welcome = states.GameScene(f"Welcome {game.player._name} !\n")
    welcome.handle_events()
    game.window.blit(game.bg, (0, 0))
    welcome.display_text()
    time.sleep(2)

    continue_game = True

    # <<<<------ MAIN GAME LOOP ------>>>>
    while continue_game:
        # Enemy creation
        # Depending on player's level, the enemy may have some advanced equipment
        if game.player.level < 5:
            settings = func.autogen(constants.GENDERS, constants.RACES, constants.MALE_NAMES, constants.FEMALE_NAMES,
                               constants.OTHER_NAMES, [items.corset, items.rags, items.rags, items.rags, items.corset,
                                                       items.underwear, items.leathersuit],
                               [items.scissors, items.fists, items.fists, items.fists, items.scissors, items.club,
                                items.dagger],
                               [items.scorch, items.wasp_stings, items.wasp_stings, items.no_spell, items.no_spell,
                                items.no_spell])
        elif game.player.level >= 5:
            settings = func.autogen(constants.GENDERS, constants.RACES, constants.MALE_NAMES, constants.FEMALE_NAMES,
                               constants.OTHER_NAMES, [items.corset, items.corset, items.platemail, items.leathersuit,
                                                       items.leathersuit, items.leathersuit, items.platemail,
                                                       items.mithril_jacket],
                               [items.halbert, items.halbert, items.club, items.scythe, items.dagger, items.dagger,
                                items.dagger],
                               [items.lightning, items.venom_gaze, items.scorch, items.blizzard, items.blizzard,
                                items.venom_gaze, items.no_spell])
        game.enemy = char.Character(**settings)



        # Stop intro music when shopping or fighting starts

        # Shop and equip phases (play 'The path of the goblin king')

        # Fight phase (play randomly 'Killers' or 'Crossing the chasm')


        continue_game = False

    ##################################
    # END of the game :

    scn.endgame.handle_events()
    scn.endgame.play_music(-1)
    game.window.blit(game.bg, (0, 0))
    scn.endgame.display_text((70, 150), game.font_big)
    game.clock.tick(constants.FPS)
    time.sleep(5)

    scn.credits.handle_events()
    game.window.blit(game.bg, (0, 0))
    scn.credits.display_text((70, 100))
    time.sleep(5)
    scn.credits.stop_music()
    time.sleep(5)
    pygame.quit()
    quit()
    ####################################





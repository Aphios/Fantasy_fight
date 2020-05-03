"""Fantasy Fight Project. A simple fight game with fantasy characters.

This file contains the main game loop.
"""

__version__ = 0.2
__author__ = "Sophie Blanchard"
__status__ = "Prototype"
__start_date__ = "03-17-2020"
__last_update__ = "05-03-2020"


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

    # *********--- INTRO ---**********
    # First, handle events (for instance : quit)
    scn.title.handle_events()
    # Launch ambiant music
    scn.title.play_music(-1)
    # Always display the background when a new scene is displayed
    game.window.blit(game.screen, (0, 0))
    # Display text
    scn.title.display_text((280, 270), game.font_big)
    time.sleep(3)
    # Control the FPS flow
    game.clock.tick(constants.FPS)

    # STORY DISPLAY
    scn.story.handle_events()
    game.window.blit(game.bg, (0, 0))
    # Display text with continue button
    scn.story.display_text_continue()
    game.clock.tick(constants.FPS)
    # Pause before displaying rules
    scn.pause.handle_events()
    # RULES DISPLAY
    scn.rules.handle_events()
    game.window.blit(game.bg, (0, 0))
    scn.rules.display_text_continue()
    game.clock.tick(constants.FPS)
    scn.pause.handle_events()
    # TIPS DISPLAY
    scn.tips.handle_events()
    game.window.blit(game.bg, (0, 0))
    scn.tips.display_text_continue()
    game.clock.tick(constants.FPS)
    scn.pause.handle_events()

    # PLAYER CREATION
    # PLAYER'S NAME
    scn.enter_name.handle_events()
    game.window.blit(game.bg, (0, 0))
    # Display the input box
    scn.enter_name.ask_user()
    # Retrieve the user's answer
    p_name = game.get_ui()
    # Don't forget to clear the game's input box before re-using
    game.input_box.clear()
    # PLAYER'S GENDER
    # Verify the input is authorized before retrieving it
    p_gender = ''
    while not func.verify_ui(p_gender, constants.GENDERS):
        scn.enter_gender.handle_events()
        game.window.blit(game.bg, (0, 0))
        scn.enter_gender.ask_user()
        p_gender = game.get_ui()
    # PLAYER'S RACE
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
    game.clock.tick(constants.FPS)

    continue_game = True

    # <<<<------ MAIN GAME LOOP ------>>>>
    while continue_game:
        # ENEMY CREATION
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
        # Save the enemy as a game attribute
        game.enemy = char.Character(**settings)

        # VIEWING STATS AND INVENTORY
        scn.view_stats.handle_events()
        game.window.blit(game.bg, (0, 0))
        # Displaying the yes/no buttons to give the player the choice to view their stats or skip this scene
        scn.view_stats.display_text_yesno((20, 300))
        game.clock.tick(constants.FPS)
        view = scn.yes_no.handle_events()
        if view:
            game.window.blit(game.bg, (0, 0))
            # for a reason yet unknown, we can't use the GameScene display_text_continue function with a
            # string that is a result of a function, so we have to use the raw game functions blit_text and blit_button
            game.blit_text(str(game.player), (10, 20), game.font_small, constants.BLACK)
            game.continue_button.blit_button(game.window, constants.GOLD)
            pygame.display.flip()
            game.clock.tick(constants.FPS)
            scn.pause.handle_events()

        # GOING TO SHOP
        scn.go_shop.handle_events()
        game.window.blit(game.bg, (0, 0))
        scn.go_shop.display_text_yesno((20, 300))
        game.clock.tick(constants.FPS)
        shoping = scn.yes_no.handle_events()
        game.window.blit(game.bg, (0, 0))
        if shoping:
            # Fadeout intro music
            scn.go_shop.stop_music(2000)
            game.blit_text("--Welcome to 'Fighters Bazaar' !--", (50, 250), game.font_big, constants.BLACK)
            pygame.display.flip()
            time.sleep(2.30)
            game.clock.tick(constants.FPS)
            continue_shop = True
            # New music for shopping and equiping player
            scn.shop_menu.play_music(-1)
            while continue_shop:
                game.input_box.clear()
                p_choice = ''
                # We want to know if the player wants to buy, sell or exit the shop
                # SHOP LOOP
                while not func.verify_ui(p_choice, ['Buy', 'Sell', 'Exit']):
                    scn.shop_menu.handle_events()
                    game.window.blit(game.bg, (0, 0))
                    scn.shop_menu.ask_user()
                    p_choice = game.get_ui()

                # SELL ITEM
                if p_choice == 'Sell' and game.player.available_items():
                    item_sell = ''
                    while not func.verify_ui(item_to_sell, game.player.available_items()):
                        game.input_box.clear()
                        scn.inventory_choose.handle_events()
                        game.window.blit(game.bg, (0, 0))
                        game.blit_text("Here's your inventory. Choose what you wish to sell.\n", (10, 20),
                                       game.font_small, constants.BLACK)
                        game.blit_text(game.player.display_inventory(), (10, 100), game.font_small, constants.BLACK)
                        scn.inventory_choose.ask_user((30, 420))
                        item_sell = game.get_ui()
                    if item_sell == 'Nothing':
                        continue
                    else :
                        trade = game.player.sell(item_sell)
                        game.handle_events()
                        game.window.blit(game.bg, (0, 0))
                        print_sell = states.GameScene(trade)
                        print_sell.display_text_continue()
                        game.clock.tick(constants.FPS)
                        scn.pause.handle_events()
                # If the player have no item to sell, they return to the beginning of the shop loop
                elif p_choice == 'Sell' and not game.player.available_items():
                    scn.no_sell.handle_events()
                    game.window.blit(game.bg, (0, 0))
                    scn.no_sell.display_text_continue()
                    game.clock.tick(constants.FPS)
                    scn.pause.handle_events()

                # BUY ITEM
                elif p_choice == 'Buy':
                    look_stock = ''
                    item_buy = ''
                    # We ask the player from which stocks they wish to make a purchase
                    while not func.verify_ui(look_stock, ['Armours', 'Spells', 'Weapons']):
                        game.input_box.clear()
                        scn.which_stock.handle_events()
                        game.window.blit(game.bg, (0, 0))
                        scn.which_stock.ask_user()
                        look_stock = game.get_ui()

                    # DISPLAY ARMOUR STOCKS
                    if look_stock == 'Armours':
                        while not func.verify_ui(item_buy, items.shop.list_armour_sales):
                            game.input_box.clear()
                            scn.shop_stocks.handle_events()
                            game.window.blit(game.bg, (0, 0))
                            trade = items.shop.display_armour()
                            game.blit_text(trade, (10, 20), game.font_small, constants.BLACK)
                            scn.shop_stocks.ask_user((10, 250))
                            item_buy = game.get_ui()

                    # DISPLAY WEAPON STOCKS
                    elif look_stock == 'Weapons':
                        while not func.verify_ui(item_buy, items.shop.list_weapon_sales):
                            game.input_box.clear()
                            scn.shop_stocks.handle_events()
                            game.window.blit(game.bg, (0, 0))
                            trade = items.shop.display_weapon()
                            game.blit_text(trade, (10, 20), game.font_small, constants.BLACK)
                            scn.shop_stocks.ask_user((10, 250))
                            item_buy = game.get_ui()

                    # DISPLAY SPELL STOCKS
                    elif look_stock == 'Spells':
                        while not func.verify_ui(item_buy, items.shop.list_spell_sales):
                            game.input_box.clear()
                            scn.shop_stocks.handle_events()
                            game.window.blit(game.bg, (0, 0))
                            trade = items.shop.display_spell()
                            game.blit_text(trade, (10, 20), game.font_small, constants.BLACK)
                            scn.shop_stocks.ask_user((10, 250))
                            item_buy = game.get_ui()

                    # BUY ITEM
                    # If player already have the item or don't want anything, go back to the beginning of shop loop
                    if (item_buy in game.player.inventory or item_buy == game.player.weapon.name
                        or item_buy == game.player.spell.name or item_buy == game.player.armour.name):
                        scn.already_yours.handle_events()
                        game.window.blit(game.bg, (0, 0))
                        scn.already_yours.display_text_continue()
                        game.clock.tick(constants.FPS)
                        scn.pause.handle_events()
                    elif item_buy == 'Nothing':
                        game.handle_events()
                        time.sleep(1.30)
                        game.clock.tick(constants.FPS)
                    else:
                        buying = game.player.buy(item_buy, items.shop)
                        game.handle_events()
                        game.window.blit(game.bg, (0, 0))
                        game.blit_text(buying, (10, 20), game.font_small, constants.BLACK)
                        game.continue_button.blit_button(game.window, constants.GOLD)
                        pygame.display.flip()
                        game.clock.tick(constants.FPS)
                        scn.pause.handle_events()

                # EXITING SHOP
                elif p_choice == 'Exit':
                    continue_shop = False

        # EQUIPING
        # Ask the player if they want to don some equipment
        scn.go_equip.handle_events()
        game.window.blit(game.bg, (0, 0))
        scn.go_equip.display_text_yesno((20, 300))
        game.clock.tick(constants.FPS)
        equiping = scn.yes_no.handle_events()
        game.window.blit(game.bg, (0, 0))
        if equiping:
            # If player didn't go shop before, it's time to switch the music
            if not shoping:
                scn.go_equip.stop_music(2000)
                time.sleep(2)
                scn.shop_menu.play_music(-1)
            continue_equip = True
            while continue_equip:
                game.input_box.clear()
                eq_item = ''
                # If the player have something in their inventory, make them choose what to equip
                if game.player.available_items():
                    while not func.verify_ui(eq_item, game.player.available_items()):
                        game.handle_events()
                        game.window.blit(game.bg, (0, 0))
                        p_inv = game.player.display_inventory()
                        game.blit_text(p_inv, (10, 20), game.font_small, constants.BLACK)
                        scn.inventory_choose.ask_user()
                        eq_item = game.get_ui()
                    if eq_item != 'Nothing':
                        game.player.equip(eq_item)
                        # Ask the player if they want to continue equiping themself
                        scn.re_equip.handle_events()
                        game.window.blit(game.bg, (0, 0))
                        scn.re_equip.display_text_yesno()
                        game.clock.tick(constants.FPS)
                        re_equiping = scn.yes_no.handle_events()
                        if not re_equiping:
                            continue_equip = False
                # If they have nothing, we end the equiping loop
                else:
                    scn.no_equip.handle_events()
                    game.window.blit(game.bg, (0, 0))
                    scn.no_equip.display_text_continue()
                    game.clock.tick(constants.FPS)
                    scn.pause.handle_events()
                    continue_equip = False

        # INTRODUCING THE ENEMY
        # Fadeout current music before introducing new one
        scn.go_equip.stop_music(2000)
        scn.enter_arena.handle_events()
        time.sleep(1)
        game.window.blit(game.bg, (0, 0))
        scn.enter_arena.display_text()
        show_enemy = str(game.enemy)
        game.blit_text(show_enemy, (10, 50), game.font_small, constants.BLACK)
        game.continue_button.blit_button(game.window)
        pygame.display.flip()
        # Launch a random fighting music
        game.play_random_music(-1)
        game.clock.tick(constants.FPS)
        scn.pause.handle_events()


        continue_game = False

    ##################################
    # END of the game :
    # Fading ancient music before introducing new one
    scn.endgame.stop_music(1500)
    scn.endgame.handle_events()
    time.sleep(1)
    scn.endgame.play_music(-1)
    game.window.blit(game.bg, (0, 0))
    scn.endgame.display_text((70, 150), game.font_big)
    game.clock.tick(constants.FPS)
    time.sleep(5)

    scn.credits.handle_events()
    game.window.blit(game.bg, (0, 0))
    scn.credits.display_text((70, 85))
    time.sleep(6)
    scn.credits.stop_music(5000)
    time.sleep(6)
    pygame.quit()
    quit()
    ####################################





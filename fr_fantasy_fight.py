"""Fantasy Fight Project. A simple fight game with fantasy characters.

This file contains the main game loop.
"""

__version__ = 0.3
__author__ = "Sophie Blanchard"
__start_date__ = "03-17-2020"
__last_update__ = "05-17-2020"

import time

import pygame

import French_version.fr_constants as constants
import French_version.fr_characters as char
import French_version.fr_game_class as game
import French_version.fr_items as items
import French_version.fr_scenes as scn
import French_version.fr_func as func
import Game.gui_elements as gui


pygame.init()

# Initialize game
game = game.Game()

# >>>>>>>>>>---- PYGAME LOOP ----<<<<<<<<<<<
launched = True
while launched:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

    # >>>>>>>>--- INTRO ----<<<<<<<<<<
    # Display title and start music
    game.text_music_sleep(scn.title, 3, game.screen, (280, 270), game.intro_music, -1, game.font_big)
    # Display the game intro texts with continue button
    game.text_img_continue(scn.story, game.bg)
    game.text_img_continue(scn.rules, game.bg)
    game.text_img_continue(scn.tips, game.bg)

    # >>>>>>>--- PLAYER CREATION ---<<<<<<<<
    # Get the player's name
    p_name = game.ask_user(scn.enter_name, game.bg)
    # Get player's gender
    p_gender = game.ask_check_img(scn.enter_gender, game.bg, constants.GENDERS)
    # Get player's race
    p_race = game.ask_check_img(scn.enter_race, game.bg, constants.RACES)
    # Register player as a game attribute
    game.player = char.Player(p_name, p_gender, p_race, items.underwear, items.fists, items.no_spell)
    # Welcome player
    game.text_wait(f"Bienvenue {game.player._name} !\n", game.bg, (250, 280), 2, constants.IMMORTAL_BIG)

    # Initialize game loop
    continue_game = True

    # Initialize the repeat fight variable (it will be used to propose the player to desequip after the fights)
    more_fight = ''

    # >>>>>>---- MAIN GAME LOOP ----<<<<<<<
    while continue_game:
        # >>>>>>>---- ENEMY CREATION ----<<<<<<<<
        # Depending on player's level, the enemy may have some advanced equipment
        if game.player.level < 5:
            settings = func.autogen(constants.GENDERS, constants.RACES, constants.MALE_NAMES, constants.FEMALE_NAMES,
                                    constants.OTHER_NAMES,
                                    [items.corset, items.rags, items.rags, items.rags, items.corset,
                                     items.underwear, items.leathersuit],
                                    [items.scissors, items.fists, items.fists, items.fists, items.scissors, items.club,
                                     items.dagger],
                                    [items.scorch, items.wasp_stings, items.wasp_stings, items.no_spell, items.no_spell,
                                     items.no_spell])
        elif game.player.level >= 5:
            settings = func.autogen(constants.GENDERS, constants.RACES, constants.MALE_NAMES, constants.FEMALE_NAMES,
                                    constants.OTHER_NAMES,
                                    [items.corset, items.corset, items.platemail, items.leathersuit,
                                     items.leathersuit, items.leathersuit, items.platemail,
                                     items.mithril_jacket],
                                    [items.halbert, items.halbert, items.club, items.scythe, items.dagger, items.dagger,
                                     items.dagger],
                                    [items.lightning, items.venom_gaze, items.scorch, items.blizzard, items.blizzard,
                                     items.venom_gaze, items.no_spell])
        # Save the enemy as a game attribute
        game.enemy = char.Character(**settings)

        # >>>>>>>---- VIEW STATS AND INVENTORY ----<<<<<<
        # Player can skip this scene if they don't want to look at their stats
        view = game.text_yesno(scn.view_stats, game.bg)
        if view:
            game.text_img_continue(str(game.player), game.bg, picture=game.player.pic, pos_picture=(550, 70))

        # >>>>>>---- SHOP -----<<<<<<<<<
        # Player can skip thse scene if they don't want to go shop
        shoping = game.text_yesno(scn.go_shop, game.bg)
        if shoping:
            # We display the name of the shop while changing the musics with a light transition
            game.stop_music(2000)
            game.text_music_sleep(scn.bazaar, 2, game.img_shop, (120, 260), font=game.font_big, subtext=game.large_pane,
                                  subpos=(50, 125))
            game.play_music(game.shop_music)
            # Initialize shop loop
            continue_shop = True
            while continue_shop:
                # We propose the player to either buy, sell or exit the shop
                p_choice = game.ask_check_img(scn.shop_menu, game.img_shop, ['Acheter', 'Vendre', 'Sortir'], (150, 260),
                                              subtext=game.pane)
                # Sell item
                if p_choice == 'Vendre' and game.player.available_items():
                    item_sell = game.ask_check_img(game.player.display_inventory() + scn.inventory_choose,
                                                   game.img_shop, game.player.available_items(), (90, 170),
                                                   subtext=game.large_pane, subpos=(50, 125))
                    if item_sell == 'Rien':
                        continue
                    else:
                        game.text_img_continue(game.player.sell(item_sell), game.img_shop, (150, 260), subtext=game.pane)
                # If the player has no item to sell, they return to the beginning of the shop loop
                elif p_choice == 'Vendre' and not game.player.available_items():
                    game.text_img_continue(scn.no_sell, game.img_shop, (150, 260), subtext=game.pane)
                # BUY ITEM
                elif p_choice == 'Acheter':
                    # We ask the player which stocks they want to see
                    look_stock = game.ask_check_img(scn.which_stock, game.img_shop, ['Armures', 'Sorts', 'Armes'],
                                                    (150, 260), subtext=game.pane)
                    # Display armours
                    if look_stock == 'Armures':
                        item_buy = game.ask_check_img(items.shop.display_armour() + scn.shop_stocks,
                                                      game.img_shop, items.shop.list_armour_sales, (90, 170),
                                                      subtext=game.large_pane, subpos=(50, 125))
                    # Display weapons
                    elif look_stock == 'Armes':
                        item_buy = game.ask_check_img(items.shop.display_weapon() + scn.shop_stocks, game.img_shop,
                                                      items.shop.list_weapon_sales, (90, 170),
                                                      subtext=game.large_pane, subpos=(50, 125))
                    # Display spells
                    elif look_stock == 'Sorts':
                        item_buy = game.ask_check_img(items.shop.display_spell() + scn.shop_stocks, game.img_shop,
                                                      items.shop.list_spell_sales, (90, 170),
                                                      subtext=game.large_pane, subpos=(50, 125))

                    # Make the transaction
                    # If player already have the item or don't want anything, go back to the beginning of shop loop
                    if item_buy == 'Rien':
                        continue
                    elif (item_buy in game.player.inventory or item_buy == game.player.weapon.name
                        or item_buy == game.player.spell.name or item_buy == game.player.armour.name):
                        game.text_img_continue(scn.already_yours, game.img_shop, (150, 260), subtext=game.pane)
                    else:
                        game.text_img_continue(game.player.buy(item_buy, items.shop), game.img_shop, (150, 260),
                                               subtext=game.pane)

                # EXITING SHOP
                elif p_choice == 'Sortir':
                    time.sleep(1)
                    continue_shop = False

        # EQUIPING
        # Ask the player if they want to don some equipment
        equiping = game.text_yesno(scn.go_equip, game.bg)
        if equiping:
            # If player didn't go shop before, it's time to switch the musics
            if not shoping:
                game.stop_music(2000)
                game.text_music_sleep(scn.your_pack, 2, game.bg, (50, 250), font=game.font_big)
                game.play_music(game.shop_music)
            # Initialize equip loop
            continue_equip = True
            while continue_equip:
                # If the player have something in their inventory, make them choose what to equip
                if game.player.available_items():
                    eq_item = game.ask_check_img(game.player.display_inventory() + scn.inventory_choose, game.bg,
                                                 game.player.available_items())
                    if eq_item != 'Rien':
                        game.player.equip(eq_item)
                        re_equiping = game.text_yesno(scn.re_equip, game.bg)
                        if not re_equiping:
                            continue_equip = False
                # If player as nothing to equip, we end the equiping loop
                else:
                    game.text_img_continue(scn.no_equip, game.bg, (50, 250))
                    continue_equip = False

        # >>>>>>---- INTRODUCING THE ENEMY ----<<<<<<<<<
        # Fadeout current music before introducing new one
        game.stop_music(2000)
        game.text_music_sleep(scn.enter_arena, 2, game.bg, (50, 250), font=game.font_big)
        game.play_random_music()
        # Display the enemy's stats
        game.text_img_continue(str(game.enemy), game.img_arena, (40, 45), subtext=game.large_pane, subpos=(10, 20),
                               picture2=game.enemy.pic)

        # >>>>>>>---- FIGHT -----<<<<<<<
        # Save starting life points for future restoration
        reset_life = game.player.life
        while True:
            # TURN BY TURN
            # Player chooses their attack and hits
            attack = game.ask_check_img(game.player.choose_attack(), game.img_arena, game.player.available_attacks(),
                                        (20, 30), picture=game.player.pic, picture2=game.enemy.pic)
            game.text_img_continue(game.player.hit(game.enemy, attack), game.img_arena, picture=game.player.pic,
                                   picture2=game.enemy.pic)
            if game.enemy.life <= 0:
                break
            # Enemy "chooses" their attack and hits
            counterattack = game.enemy.random_attack()
            game.text_img_continue(game.enemy.hit(game.player, counterattack), game.img_arena,
                                   font_color=constants.BURGUNDY, picture=game.player.pic, picture2=game.enemy.pic)
            if game.player.life <= 0:
                break

        # If player wins : reset life to full, gain xp, add a win and loot
        fight_result = game.player.win_or_loose(game.enemy)
        if fight_result == "Vous remportez le combat !\n":
            game.player.life = reset_life
            game.text_img_continue(fight_result + game.player.gain_xp(game.enemy), game.img_arena,
                                   picture=game.player.pic)
            while game.player.experience >= constants.XP_LEVELS[str(game.player.level)]:
                game.text_img_continue(game.player.level_up(), game.img_arena, picture=game.player.pic)
            game.player.wins += 1
            game.text_img_continue(game.player.loot(), game.img_arena, picture=game.player.pic)
        # If player looses go to THE END
        else:
            game.text_img_continue(fight_result, game.img_arena)
            break

        # Propose player to start another fight if they haven't reached last level. If not, stop the game.
        if game.player.level < 10:
            more_fight = game.text_yesno(scn.fight_again, game.img_arena, (20, 30))
            if not more_fight:
                continue_game = False
        # If player has reached the last level, congratulate them and stop the game.
        if game.player.level >= 10:
            game.text_img_continue(scn.last_level, game.img_arena, (20, 30))
            continue_game = False

    # >>>>>>>----- THE END -------<<<<<<<<<<
    # Fading ancient music before playing new one
    game.stop_music(5000)
    game.text_img_continue(game.player.achievements(), game.bg, (70, 150), picture=game.player.pic,
                           pos_picture=(550, 150))
    game.text_music_sleep(scn.endgame, 6, game.bg, (70, 150), game.intro_music, -1, game.font_big)
    # Display credits
    game.text_music_sleep(scn.credits, 8, game.bg, (70, 85))
    game.text_music_sleep(scn.credits2, 2, game.bg, (70, 150))
    game.stop_music(4000)
    time.sleep(4)
    # Automatically quit program
    pygame.quit()
    quit()





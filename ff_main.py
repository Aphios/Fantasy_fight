"""Fantasy Fight Project. A  simple fight game with fantasy characters.

This file contains the main game functions and textual elements to be passed to pygame (in module ff_game).
"""

__version__ = 0.2
__author__ = "Sophie Blanchard"
__status__ = "Prototype"
__start_date__ = "03-17-2020"
__last_update__ = "04-27-2020"


# Text elements
# TODO : transpose them into game functions
# Player creation
create_player = "Let's start !\nEnter your character's name (anything will work and you can't go back so don't write " \
                "crap unless you really mean to) : \n"
create_player_2 = "\nNow choose your race !\n~Githzerais are agile and stealthy, but not so clever. They are healthy " \
                  "but lack strength.\n~Banshees are really clever but not so full of life and they definitely lack " \
                  "strength.\n~Tieflins are absolutely dumb but very strong and well built.\n~Illithids are madly " \
                  "clever but rather frail.\n~Rakshasas are very strong and resisting, but nearly as dumb as " \
                  "Tieflins.\n"

# Shop
welcome_shop = "--Welcome to 'Fighters Bazaar' !--"
no_sell = "You have nothing to sell.\n"
inventory_choose = "Here's your inventory. Choose what you wish to sell.\n"
buy_shop = "Here are the items available for sale. Choose what you wish to buy.\n"
already_yours = "You already have this item in your posession.\n"
which_stock = "Which stocks do you wish to look at ?\n"

# Equip
inventory_equip = "Here's your inventory. Choose what you wish to equip.\n"
no_equip = "You have nothing to equip !\n"

# Fight
enter_arena = "You meet your opponent in the arena : \n"
last_level = "You have reached the last level and defeated all your enemies !\n"

# Main program
if __name__ == '__main__':
    import random
    import time
    import pyinputplus as pyip
    import ff_classes as ffc

    # <<<<------ GAME INITIALIZATION ------>>>>

    # Initialize on-going game
    continue_game = True

    # Introducing the game
    start_game()

    # Player creation
    p_name = input(create_player)
    p_gender = pyip.inputMenu(ffc.GENDERS, numbered=True)
    print(create_player_2)
    p_race = pyip.inputMenu(ffc.RACES, numbered=True)
    player = ffc.Player(p_name, p_gender, p_race, underwear, fists, no_spell)

    # <<<<------ MAIN GAME LOOP ------>>>>

    while continue_game:
        # Enemy creation
        # Depending on player's level, the enemy may have some advanced equipment
        if player.level < 5:
            settings = autogen(ffc.GENDERS, ffc.RACES, ffc.MALE_NAMES, ffc.FEMALE_NAMES, ffc.OTHER_NAMES,
                               [corset, rags, rags, rags, corset, underwear, leathersuit],
                               [scissors, fists, fists, fists, scissors, club, dagger],
                               [scorch, wasp_stings, wasp_stings, no_spell, no_spell, no_spell])
        elif player.level >= 5:
            settings = autogen(ffc.GENDERS, ffc.RACES, ffc.MALE_NAMES, ffc.FEMALE_NAMES, ffc.OTHER_NAMES,
                               [corset, corset, platemail, leathersuit, leathersuit, leathersuit, platemail,
                                mithril_jacket], [halbert, halbert, club, scythe, dagger, dagger, dagger],
                               [lightning, venom_gaze, scorch, blizzard, blizzard, venom_gaze, no_spell])
        enemy = ffc.Character(**settings)

        # Propose the player to view their stats and inventory
        print(f"Welcome {player._name} !")
        view_stats = pyip.inputYesNo("Do you want to view your stats and equipment ? (Yes/No)\n")
        if view_stats == 'yes':
            print(player)
            player.display_inventory()

        # Propose the player to go shop
        to_shop = pyip.inputYesNo("\nDo you want to go to the Shop to buy or sell some equipment ? (Yes/No)\n")

        # SHOPPING LOOP
        if to_shop == 'yes':
            print(welcome_shop)
            continue_shop = True

            while continue_shop:
                # Shop menu
                buy_or_sell = pyip.inputMenu(['Buy', 'Sell', 'Exit shop'], numbered=True)

                # If player has nothing to sell, go back to shop menu
                if buy_or_sell == 'Sell' and not player.available_items():
                    print(no_sell)
                    continue
                # If player may sell something, make the deal
                elif buy_or_sell == 'Sell' and player.available_items():
                    print(inventory_choose)
                    player.display_inventory()
                    print("\n")
                    time.sleep(2)
                    selling = pyip.inputMenu(player.available_items(), numbered=True)
                    if selling == 'Nothing':
                        continue
                    else:
                        player.sell(selling)

                # Or buy something if the player doesn't already have the item in their posession
                elif buy_or_sell == 'Buy':
                    print(which_stock)
                    stock_type = pyip.inputMenu(['Armours', 'Weapons', 'Spells'], numbered=True)
                    print(buy_shop)
                    buying = 'Nothing'

                    if stock_type == 'Armours':
                        shop.display_armour()
                        print("\n")
                        buying = pyip.inputMenu(shop.list_armour_sales, numbered=True)
                    elif stock_type == 'Spells':
                        shop.display_spell()
                        print("\n")
                        buying = pyip.inputMenu(shop.list_spell_sales, numbered=True)
                    elif stock_type== 'Weapons':
                        shop.display_weapon()
                        print("\n")
                        buying = pyip.inputMenu(shop.list_weapon_sales_sales, numbered=True)

                    if buying == 'Nothing':
                        continue
                    if (buying in player.inventory or buying == player.weapon.name or buying == player.spell.name or
                            buying == player.armour.name):
                        print(already_yours)
                        continue
                    else:
                        player.buy(buying, shop)

                # Exit shop when done
                elif buy_or_sell == 'Exit shop':
                    continue_shop = False

        # EQUIP LOOP
        to_equip = pyip.inputYesNo("Do you wish to equip yourself before going to fight ? (Yes/No)\n")
        if to_equip == 'yes':
            continue_equip = True
            while continue_equip:
                if player.available_items():
                    # Make the player choose from their inventories one or more objects to equip
                    print(inventory_equip)
                    player.display_inventory()
                    print("\n")
                    equiping = pyip.inputMenu(player.available_items(), numbered=True)
                    if equiping != 'Nothing':
                        player.equip(equiping)
                    re_equip = pyip.inputYesNo('Do you want to continue changing your equipment ? (Yes/No)\n')
                    if re_equip == 'no':
                        continue_equip = False
                else:
                    print(no_equip)
                    continue_equip = False

        # FIGHT LOOP
        # Introduce the opponent
        print(enter_arena)
        print(enemy)
        time.sleep(7)
        # Save starting life points for future restoration
        reset_life = player.life
        while True:
            # Alternate player and enemy's blows until one of them is dead
            # Player chooses their attack and hits
            attack = player.choose_attack()
            player.hit(enemy, attack)
            if enemy.life <= 0:
                break
            # Enemy "chooses" their attack and hits
            counterattack = enemy.random_attack()
            enemy.hit(player, counterattack)
            if player.life <= 0:
                break

        # If player wins : reset life to full, gain xp, add 1 to player.wins and loot.
        if player.win_or_loose(enemy):
            player.life = reset_life
            player.gain_xp(enemy)
            player.wins += 1
            player.loot()
        # If player looses go to end game.
        else:
            break

        # Propose player to start another fight if they haven't reached last level. If not, stop the game.
        if player.level < 10:
            if pyip.inputYesNo("Do you want to fight another adversary ? (Yes/No)\n") == 'no':
                continue_game = False
        # If player has reached the last level, congratulate them and stop the game.
        if player.level >= 10:
            print(last_level)
            continue_game = False

    # >>> END GAME <<<
    player.achievements()
    print(game_over_msg)
    time.sleep(3)
    print(credits)
    raise SystemExit(0)

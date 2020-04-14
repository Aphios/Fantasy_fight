"""Fantasy Fight Project

-- Version 0.1
Author : Sophie Blanchard
Purpose : simple fight game with fantasy characters
Start date : 03-17-2020
Last update : 04-14-2020

This file contains the main program and general functions.
"""


# Main functions
def start_game():
    """Prints the game pitch and rules"""
    print("Welcome fo Fantasy Fight !\nFantasy Fight is a basic 'read and choose' game.\n")
    print("~~~STORY~~~\nYou enter the Forgotten Realms, a fantasy world where heroes fight for power and glory.\n")
    print("~~~GOAL~~~\nYour goal is to defeat as many enemies as you can and gain eternal renoun !\n")
    print("~~~RULES~~~\nYou will create a character and be given some money (or not if you're unluncky !) to buy "
          "some equipment.\nYou can choose to be a Rakshasa, an Illithid, a Tieflin, a Banshee or a Githzerai.\nFrom"
          " your race depends your life force, your strength, your intelligence and your special ability.\n"
          "You will be able to buy weapons, armours and spells. You can also sell equipment in your inventory.\nYou"
          " cannot sell your current weapon, spell or armour unless you equip something else.\nThen you will fight "
          "other characters until you die or choose to retire.\nEach enemy defeated is rewarded by experience points "
          "and a chance to loot some gold.\nWhen you have earned enough experience, you will gain a level and your "
          "stats will increase.\n")
    print("~~~Fighting tips~~~\nBefore entering a fight, know that :\n- you may cause damage to your enemy with "
          "your weapon (the more strong you are, the more damage you do),\n with your spell (the more clever "
          "you are, the more damage you do),\n or with your ability (this one is tricky : it can make a lot of "
          "damage but has also a more important fail risk.)\n- there is always a chance that your blow "
          "(or your adversary's) might fail.\n")
    print("~~~Ending game~~~\nYou may quit the game at any time.\nCaution ! This game does NOT save your character "
          "or your stats. It is a one-shot game !\nGood luck, and have fun !")


def autogen(genders, races, male_names, female_names, other_names, armours, weapons, spells):
    """Generates random settings for a character.
    The function returns a name, a gender a race, a weapon, an armour and a spell.
    """
    gender = random.choice(genders)
    race = random.choice(races)
    if gender == 'Male':
        name = random.choice(male_names)
    elif gender == 'Female':
        name = random.choice(female_names)
    else:
        name = random.choice(other_names)
    armour = random.choice(armours)
    weapon = random.choice(weapons)
    spell = random.choice(spells)
    return {'name': name, 'gender': gender, 'race': race, 'armour': armour, 'weapon': weapon, 'spell': spell}


def end_game(user):
    """Prints player's achievements, game over message then waits before exiting program."""
    user.achievements()
    print("~~~Game over~~~\nThank you for playing !\n~~~CREDITS~~~\nConception & programming : Aphios")
    time.sleep(10)
    #Quit program
    # TODO


# Main program
if __name__ == '__main__':
    import random
    import time
    import pyinputplus as pyip
    import ff_classes as ffc
    import ff_func as fff

    # <<<<------ GAME INITIALIZATION ------>>>>

    # Initialize on-going game
    continue_game = True

    # Individual equipment creation
    corset = ffc.Armour('Corset', 100, 4)
    leathersuit = ffc.Armour('Leathersuit', 250, 8)
    rags = ffc.Armour('Rags', 10, 1)
    underwear = ffc.Armour('Underwear', 0, 0)
    platemail = ffc.Armour('Platemail', 700, 15)
    mithril_jacket = ffc.Armour('Mithril jacket', 1500, 25)
    blizzard = ffc.Spell('Blizzard', 200, 8, 16)
    scorch = ffc.Spell('Scorch', 100, 4, 10)
    venom_gaze = ffc.Spell('Venom gaze', 150, 6, 20)
    wasp_stings = ffc.Spell('Wasp stings', 50, -5, 6)
    lightning = ffc.Spell('Lightning', 400, 18, 28)
    no_spell = ffc.Spell('No spell', 0, 0, 0)
    scythe = ffc.Weapon('Scythe', 400, 18, 28)
    scissors = ffc.Weapon('Scissors', 50, -5, 6)
    halbert = ffc.Weapon('Halbert', 200, 8, 16)
    club = ffc.Weapon('Club', 100, 4, 10)
    dagger = ffc.Weapon('Dagger', 150, 6, 20)
    fists = ffc.Weapon('Fists', 0, -8, 4)

    # Inventories and shop creation
    stocks = {'Corset': corset, 'Leathersuit': leathersuit, 'Rags': rags, 'Platemail': platemail,
              'Mithril jacket': mithril_jacket, 'Blizzard': blizzard, 'Scorch': scorch, 'Venom gaze': venom_gaze,
              'Wasp stings': wasp_stings, 'Lightning': lightning, 'Scythe': scythe, 'Scissors': scissors,
              'Halbert': halbert, 'Club': club, 'Dagger': dagger}
    shop = ffc.Shop(stocks)

    # Introducing the game
    start_game()

    # Player creation
    p_name = input("Enter your character's name (anything will work and you can't go back so don't write crap unless"
                   "you really mean to) : ")
    p_gender = pyip.inputMenu(ffc.GENDERS)
    print("Now choose your race !\n~Githzerais are agile and stealthy, but not so clever. They are healthy but lack "
          "strength.\nBanshees are really clever but not so full of life and they definitely lack strength.\n Tieflins"
          "are absolutely dumb but very strong and well built.\n Illithids are madly clever but rather frail.\n"
          "Rakshasas are very strong and resisting, but nearly as dumb as Tieflins.")
    p_race = pyip.inputMenu(ffc.RACES, numbered=True)
    player = ffc.Player(p_name, p_gender, p_race, underwear, fists, no_spell)

    print(f"Welcome {player._name} !")

    # <<<<------ MAIN GAME LOOP ------>>>>

    while continue_game:
        # Enemy creation
        # Depending on player's level, the enemy may have some advanced equipment
        if player.level < 5:
            settings = autogen(ffc.GENDERS, ffc.RACES, ffc.MALE_NAMES, ffc.FEMALE_NAMES, ffc.OTHER_NAMES,
                               [corset, rags, leathersuit], [scissors, fists, dagger], [scorch, wasp_stings, no_spell])
        elif player.level >= 5:
            settings = autogen(ffc.GENDERS, ffc.RACES, ffc.MALE_NAMES, ffc.FEMALE_NAMES, ffc.OTHER_NAMES,
                               [corset, platemail, leathersuit, mithril_jacket], [halbert, club, scythe, dagger],
                               [lightning, venom_gaze, scorch, blizzard])
        enemy = ffc.Character(**settings)

        # Propose the player to view their stats and inventory
        view_stats = pyip.inputYesNo("Do you want to view your stats and equipment ? (Yes/No)")
        if view_stats == 'yes':
            print(player)
            player.display_inventory()

        # Propose the player to go shop
        to_shop = pyip.inputYesNo("Do you want to go to the Shop to buy or sell some equipment ? (Yes/No)")

        # SHOPPING LOOP
        if to_shop == 'yes':
            print("--Welcome to 'Fighters Bazaar' !--")
            continue_shop = True

            while continue_shop:
                # Shop menu
                buy_or_sell = pyip.inputMenu(['Buy', 'Sell', 'Exit shop'], numbered=True)

                # If player has nothing to sell, go back to shop menu
                if buy_or_sell == 'Sell' and not player.available_items():
                    print("You have nothing to sell.")
                    continue
                # If player may sell something, make the deal
                elif buy_or_sell == 'Sell' and player.available_items():
                    print("Here's your inventory. Choose what you wish to sell.")
                    player.display_inventory()
                    time.sleep(2)
                    selling = pyip.inputMenu(player.available_items())
                    if selling == 'Nothing':
                        continue
                    else:
                        player.sell(selling)

                # Or buy something if the player doesn't already have the item in their posession
                elif buy_or_sell == 'Buy':
                    print("Here are the items available for sale. Choose what you wish to buy.")
                    shop.display()
                    time.sleep(2)
                    buying = pyip.inputMenu(shop.list_sales)
                    if buying == 'Nothing':
                        continue
                    if (buying in player.inventory or buying == player.weapon.name or buying == player.spell.name or
                            buying == player.armour.name):
                        print("You already have this item in your posession")
                        continue
                    else:
                        player.buy(buying, shop)

                # Exit shop when done
                elif buy_or_sell == 'Exit shop':
                    continue_shop = False

        # EQUIP LOOP
        to_equip = pyip.inputYesNo("Do you wish to equip yourself before going to fight ? (Yes/No)")
        if to_equip == 'yes':
            continue_equip = True
            while continue_equip:
                # Make the player choose from their inventories one or more objects to equip
                print("Here's your inventory. Choose what you wish to equip.")
                player.display_inventory()
                equiping = pyip.inputMenu(player.available_items())
                if equiping != 'Nothing':
                    player.equip(equiping)
                re_equip = pyip.inputYesNo('Do you want to continue changing your equipment ? (Yes/No')
                if re_equip == 'no':
                    continue_equip = False

        # FIGHT LOOP
        # Introduce the opponent
        print("You meet your opponent at the sparing grounds : ")
        print(enemy)
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
        if player.win_or_loose():
            player.life = reset_life
            player.gain_xp(enemy)
            player.wins += 1
            player.loot()
        # If player looses go to end game.
        else:
            break

        # Propose player to start another fight if they haven't reached last level. If not, stop the game.
        if player.level < 10:
            if pyip.inputYesNo("Do you want to fight another adversary ? (Yes/No)") == 'no':
                continue_game = False
        # If player has reached the last level, congratulate them and stop the game.
        if player.level >= 10:
            print("You have reached the last level and defeated all your enemies !")
            continue_game = False

    # >>> END GAME <<<
    end_game()

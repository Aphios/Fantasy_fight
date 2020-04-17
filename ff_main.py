"""Fantasy Fight Project. A  simple fight game with fantasy characters.

This file contains the main game program and general functions.
"""

__version__ = 0.2
__author__ = "Sophie Blanchard"
__status__ = "Prototype"
__start_date__ = "03-17-2020"
__last_update__ = "04-17-2020"

# Main functions
def start_game():
    """Prints the game pitch and rules"""
    print("Welcome fo Fantasy Fight !\nFantasy Fight is a basic 'read and choose' game.\n")
    time.sleep(2)
    print("~~~STORY~~~\nYou enter the Forgotten Realms, a fantasy world where heroes fight for power and glory.\n")
    time.sleep(2)
    print("~~~GOAL~~~\nYour goal is to defeat as many enemies as you can and gain eternal renoun !\n")
    time.sleep(3)
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
          "or your stats. It is a one-shot game !\nGood luck, and have fun !\n")


def autogen(genders, races, male_names, female_names, other_names, armours, weapons, spells):
    """Generates random settings for a character.

    Returns : a dict containing a name, a gender, a race, a weapon, an armour and a spell.
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
    # Quit program
    raise SystemExit(0)


# Main program
if __name__ == '__main__':
    import random
    import time
    import pyinputplus as pyip
    import ff_classes as ffc

    # <<<<------ GAME INITIALIZATION ------>>>>

    # Initialize on-going game
    continue_game = True

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

    # Introducing the game
    start_game()

    # Player creation
    p_name = input("Let's start !\nEnter your character's name (anything will work and you can't go back so don't write crap unless"
                   "you really mean to) : \n")
    p_gender = pyip.inputMenu(ffc.GENDERS, numbered=True)
    print("\nNow choose your race !\n~Githzerais are agile and stealthy, but not so clever. They are healthy but lack "
          "strength.\n~Banshees are really clever but not so full of life and they definitely lack strength.\n~Tieflins"
          " are absolutely dumb but very strong and well built.\n~Illithids are madly clever but rather frail.\n"
          "~Rakshasas are very strong and resisting, but nearly as dumb as Tieflins.\n")
    p_race = pyip.inputMenu(ffc.RACES, numbered=True)
    player = ffc.Player(p_name, p_gender, p_race, underwear, fists, no_spell)

    print(f"Welcome {player._name} !")

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
        view_stats = pyip.inputYesNo("Do you want to view your stats and equipment ? (Yes/No)\n")
        if view_stats == 'yes':
            print(player)
            player.display_inventory()

        # Propose the player to go shop
        to_shop = pyip.inputYesNo("\nDo you want to go to the Shop to buy or sell some equipment ? (Yes/No)\n")

        # SHOPPING LOOP
        if to_shop == 'yes':
            print("--Welcome to 'Fighters Bazaar' !--")
            continue_shop = True

            while continue_shop:
                # Shop menu
                buy_or_sell = pyip.inputMenu(['Buy', 'Sell', 'Exit shop'], numbered=True)

                # If player has nothing to sell, go back to shop menu
                if buy_or_sell == 'Sell' and not player.available_items():
                    print("You have nothing to sell.\n")
                    continue
                # If player may sell something, make the deal
                elif buy_or_sell == 'Sell' and player.available_items():
                    print("Here's your inventory. Choose what you wish to sell.\n")
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
                    print("Here are the items available for sale. Choose what you wish to buy.\n")
                    shop.display()
                    print("\n")
                    time.sleep(2)
                    buying = pyip.inputMenu(shop.list_sales, numbered=True)
                    if buying == 'Nothing':
                        continue
                    if (buying in player.inventory or buying == player.weapon.name or buying == player.spell.name or
                            buying == player.armour.name):
                        print("You already have this item in your posession.\n")
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
                    print("Here's your inventory. Choose what you wish to equip.\n")
                    player.display_inventory()
                    print("\n")
                    equiping = pyip.inputMenu(player.available_items(), numbered=True)
                    if equiping != 'Nothing':
                        player.equip(equiping)
                    re_equip = pyip.inputYesNo('Do you want to continue changing your equipment ? (Yes/No)\n')
                    if re_equip == 'no':
                        continue_equip = False
                else:
                    print("You have nothing to equip !\n")
                    continue_equip = False

        # FIGHT LOOP
        # Introduce the opponent
        print("You meet your opponent in the arena : \n")
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
            print("You have reached the last level and defeated all your enemies !\n")
            continue_game = False

    # >>> END GAME <<<
    end_game(player)

"""Fantasy Fight Project

-- Version 0.1
Author : Sophie Blanchard
Purpose : simple fight game with fantasy characters
Start date : 03-17-2020
Last update : 04-10-2020

This file contains the main program and general functions.
"""

# Main functions
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
    return {'name' : name, 'gender' : gender, 'race' : race, 'armour' : armour, 'weapon' : weapon, 'spell' : spell}


# Main program
if __name__ == '__main__':
    import random
    import time
    import pyinputplus as pyip
    import ff_classes as ffc
    import ff_func as fff

    # <<<<------ GAME INITIALIZATION ------>>>>

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

    # Inventories creation
    armours = {corset, leathersuit, rags, platemail, mithril_jacket}
    spells = {blizzard, scorch, venom_gaze, wasp_stings, lightning}
    weapons = {scythe, scissors, halbert, club, dagger}

    # Shop creation
    shop = ffc.Shop(armours, weapons, spells)

    # Introducting the game
    fff.start_game()

    # Player creation
    p_name = input("Enter your character's name (anything will work and you can't go back so don't write crap unless"
                   "you really mean to) : ")
    p_gender = pyip.inputMenu(ffc.GENDERS)
    print("Now choose your race !\n~Githzerais are agile and stealthy, but not so clever. They are healthy but lack "
          "strength.\nBanshees are really clever but not so full of life and they definitely lack strength.\n Tieflins"
          "are absolutely dumb but very strong and well built.\n Illithids are madly clever but rather frail.\n"
          "Rakshasas are very strong and resisting, but nearly as dumb as Tieflins.")
    p_race = pyip.inputMenu(ffc.RACES)
    player = ffc.Player(p_name, p_gender, p_race, underwear, fists, no_spell)

    # Enemy creation
    settings = autogen(ffc.GENDERS, ffc.RACES, ffc.MALE_NAMES, ffc.FEMALE_NAMES, ffc.OTHER_NAMES,
                       [corset, rags, leathersuit], [scissors, fists, dagger], [scorch, wasp_stings, no_spell])
    enemy = ffc.Character(**settings)

    # <<<<------ MAIN GAME LOOP ------>>>>

    # Propose the player to go shop
    to_shop = pyip.inputYesNo("Do you want to go to the Shop to buy or sell some equipment ? (Yes/No)")

    # SHOPPING LOOP
    if to_shop == 'yes':
        # Ask the player if they want to buy or sell equipment
        # If not, end loop
        # Verify player's input and restart asking if incorrect
        # If player chooses to sell but has nothing of price higher than 0, abort and restart loop
        # Ask the player if they want to see armour, weapons or spells
        # Verify player's input and restart asking if incorrect
        # Display shop stock (shop.display(shop.stock_weapon) for example)
        # Ask for the player's choice in displayed stock or 'Nothing'
        # Verify player's input and restart asking if incorrect
        # If nothing, abort and restart loop
        # buy() or sell() accordingly to player's choice
        #TODO

    # EQUIP LOOP
    # Propose the player to equip themself
    # Display player's inventory and ask the player which item they want to equip
    # Verify input and restart if incorrect
    # If player don't want to equip, end loop
    # equip() and restart loop
    #TODO

    # FIGHT LOOP
    # Entering fight : display enemy
    # ! Fight algorithm needed there !
    #TODO

    # If player wins : reset life to full, gain xp, add 1 to player.wins and loot
    #TODO

    # If player has enough xp to level up, do so and enhance player stats
    #TODO

    # Propose player to start another fight
    # Game should stop if player has reached level 10
    # Verify input and restart asking if incorrect
    # If no, print achievement message then GAME OVER
    #TODO

    # If yes, generate new enemy or enemies based on the current player's level
    # If player is level 3 or more, he may have up  to 2 opponents of 1 level lesser
    # If player is level 6 or more, he may have up to 3 opponents of 2 levels lesser (see if this needs to be balanced)
    # TODO

    # Start another loop (restart at the beginning of : <<<--- MAIN GAME LOOP --->>>)

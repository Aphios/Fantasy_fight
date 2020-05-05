"""Fantasy Fight Project. A simple fight game with fantasy characters.

This file contains the game text scenes displayed throughout the game.
"""

__version__ = 0.2
__author__ = "Sophie Blanchard"
__status__ = "Prototype"
__start_date__ = "03-17-2020"
__last_update__ = "05-05-2020"

import pygame
import random
import game_class as states

pygame.init()

# Game scenes (ordered)
# GAME INTRO
title = "Fantasy Fight\n"
story = "Fantasy Fight is a basic text adventure.\n~~~STORY~~~\nYou enter the Forgotten Realms, a fantasy world where" \
        " heroes fight for power and glory.\n~~~GOAL~~~\nYour goal is to defeat as many enemies as you can and gain" \
        " eternal renoun !"
rules = "~~~RULES~~~\nYou will create a character and be given some money (or not if you're unlucky !) to buy some "\
        "equipment.\nYou can choose to be a Rakshasa, an Illithid, a Tieflin, a Banshee or a "\
        "Githzerai.\nFrom your race depends your life force, your strength, your intelligence and "\
        "your special ability.\nYou will be able to buy weapons, armours and spells. You can also "\
        "sell equipment in your inventory.\nYou cannot sell your current weapon, spell or armour "\
        "unless you equip something else.\nThen you will fight other characters "\
        "until you die or choose to retire.\nEach enemy defeated is rewarded by experience points "\
        "and a chance to loot some gold.\nWhen you have earned enough experience, you will gain a "\
        "level and your stats will increase.\n"
tips = "~~~Fighting tips~~~\nBefore entering a fight, know that :\n- you may cause damage to your enemy with your "\
       "weapon (the more strong you are, the more damage you do),\n with your spell (the more clever"\
       "you are, the more damage you do),\n or with your ability (this one is tricky : it can make "\
        "a lot of damage but has also a more important fail risk.)\n- there is always a chance "\
        "that your blow (or your adversary's) might fail.\n~~~Ending game~~~\nYou may quit the "\
        "game at any time.\nCaution ! This game does NOT save your character or your stats. It is"\
        " a one-shot game !\nGood luck, and have fun !"

# CHARACTER CREATION
enter_name = "Let's start !\nEnter your character's name (anything will work and you can't go back so don't write "\
             "crap unless you really mean to) : \n"
enter_gender = "Are you female, male or other ?\nPlease write your answer below. (Only 'female', 'male' or 'other' " \
               "accepted)\n"
enter_race = "\nNow choose your race !\n~Githzerais are agile and stealthy, but not so clever. They are healthy but " \
             "lack strength.\n~Banshees are really clever but not so full of life and they definitely lack " \
             "strength.\n~Tieflins are absolutely dumb but very strong and well built.\n~Illithids are madly clever " \
             "but rather frail.\n~Rakshasas are very strong and resisting, but nearly as dumb as Tieflins.\nPlease " \
             "write your answer below. (Only 'Githzerai', 'Banshee', 'Tieflin', 'Illithid' or 'Rakshasa' accepted)\n"

# ENDING
endgame = "~~~Game over~~~\nThank you for playing !\n~~~CREDITS~~~\nConception & programming : Aphios\n"
credits = "Made with Python 3.7 and Pygame 1.9.6\n\nMusic:\n'The Descent' by Kevin MacLeod\nLink: "\
          "https://incompetech.filmmusic.io/song/4490-the-descent\nLicense: "\
          "http://creativecommons.org/licenses/by/4.0/\n\n'Crossing the Chasm' by Kevin MacLeod\n"\
          "Link: https://incompetech.filmmusic.io/song/3562-crossing-the-chasm\nLicense: "\
          "http://creativecommons.org/licenses/by/4.0/\n\n'Killers' by Kevin MacLeod\n"\
          "Link: https://incompetech.filmmusic.io/song/3952-killers\nLicense: "\
          "http://creativecommons.org/licenses/by/4.0/\n\n'The Path of the Goblin King' by Kevin MacLeod"\
          "\nLink: https://incompetech.filmmusic.io/song/4503-the-path-of-the-goblin-king\nLicense: "\
          "http://creativecommons.org/licenses/by/4.0/\n"

# STATS
view_stats = "Do you want to view your stats and equipment ?\n"

# SHOP
go_shop = "Do you want to go to the Shop to buy or sell some equipment ?"
bazaar = "--Welcome to 'Fighters Bazaar' !--"
shop_menu = "Do you want to buy, sell, or exit shop ?\nPlease write your answer below (only 'Buy', 'Sell' or 'Exit' " \
            "accepted)."
no_sell = "You have nothing to sell.\n"
inventory_choose = "Please write the name of one of your posessions below (or 'Nothing')."
already_yours = "You already have this item in your posession.\n"
which_stock = "Which stocks do you wish to look at ? (Please choose between 'Armours', 'Spells' or 'Weapons')\n"
shop_stocks = "\nThose are the items available for sale. Please write below the name of the item you wish to purchase," \
              " or 'Nothing'."

# EQUIP
go_equip = "Do you wish to equip yourself before going to fight ?\n"
your_pack = "Let's have a look at your pack !\n"
no_equip = "You have nothing to equip !\n"
re_equip = "Done ! Do you want to continue changing your equipment ?\n'"

# FIGHT
enter_arena = "You meet your opponent in the arena : \n"
last_level = "You have reached the last level and defeated all your enemies !\n"



"""Fantasy Fight Project. A simple fight game with fantasy characters.

This file contains the classes :
- GameScene and its subclasses
"""

__version__ = 0.2
__author__ = "Sophie Blanchard"
__status__ = "Prototype"
__start_date__ = "03-17-2020"
__last_update__ = "05-01-2020"

import pygame
import time
import constants as cst
import gui_elements as gui
import game_states as states

pygame.init()

# Game scenes (ordered)
# GAME INTRO
title = states.GameScene("Fantasy Fight\n", "Music/the-descent.mp3")
story = states.GameScene("Fantasy Fight is a basic text adventure.\n~~~STORY~~~\nYou enter the "
                              "Forgotten Realms, a fantasy world where heroes fight for power and glory.\n~~~GOAL~~~\n"
                              "Your goal is to defeat as many enemies as you can and gain eternal renoun !")
rules = states.GameScene("~~~RULES~~~\nYou will create a "
                          "character and be given some money (or not if you're unlucky !) to buy some "
                          "equipment.\nYou can choose to be a Rakshasa, an Illithid, a Tieflin, a Banshee or a "
                          "Githzerai.\nFrom your race depends your life force, your strength, your intelligence and "
                          "your special ability.\nYou will be able to buy weapons, armours and spells. You can also "
                          "sell equipment in your inventory.\nYou cannot sell your current weapon, spell or armour "
                          "unless you equip something else.\nThen you will fight other characters "
                          "until you die or choose to retire.\nEach enemy defeated is rewarded by experience points "
                          "and a chance to loot some gold.\nWhen you have earned enough experience, you will gain a "
                          "level and your stats will increase.\n")
tips = states.GameScene("~~~Fighting tips~~~\nBefore "
                          "entering a fight, know that :\n- you may cause damage to your enemy with your "
                          "weapon (the more strong you are, the more damage you do),\n with your spell (the more clever"
                          "you are, the more damage you do),\n or with your ability (this one is tricky : it can make "
                          "a lot of damage but has also a more important fail risk.)\n- there is always a chance "
                          "that your blow (or your adversary's) might fail.\n~~~Ending game~~~\nYou may quit the "
                          "game at any time.\nCaution ! This game does NOT save your character or your stats. It is"
                          " a one-shot game !\nGood luck, and have fun !")

# CHARACTER CREATION
enter_name = states.GameScene("Let's start !\nEnter your character's name (anything will work and you can't go back so don't write "
    "crap unless you really mean to) : \n")
enter_gender = states.GameScene("Are you female, male or other ?\nPlease write your answer below. (Only 'female', "
                                "'male' or 'other' accepted)\n")
enter_race = states.GameScene("\nNow choose your race !\n~Githzerais are agile and stealthy, but not so clever. They "
                              "are healthy but lack strength.\n~Banshees are really clever but not so full of life "
                              "and they definitely lack strength.\n~Tieflins are absolutely dumb but very strong and "
                              "well built.\n~Illithids are madly clever but rather frail.\n~Rakshasas are very "
                              "strong and resisting, but nearly as dumb as Tieflins.\nPlease write your answer below. "
                              "(Only 'Githzerai', 'Banshee', 'Tieflin', 'Illithid' or 'Rakshasa' accepted)\n")

# ENDING
endgame = states.GameScene("~~~Game over~~~\nThank you for playing !\n~~~CREDITS~~~\nConception & programming : "
                             "Aphios\n", "Music/the-descent.mp3")
credits = states.GameScene("Made with Python 3.7 and Pygame 1.9.6\n\nMusic:\n'The Descent' by Kevin MacLeod\nLink: "
                       "https://incompetech.filmmusic.io/song/4490-the-descent\nLicense: "
                       "http://creativecommons.org/licenses/by/4.0/\n\n'Crossing the Chasm' by Kevin MacLeod\n"
                       "Link: https://incompetech.filmmusic.io/song/3562-crossing-the-chasm\nLicense: "
                       "http://creativecommons.org/licenses/by/4.0/\n\n'Killers' by Kevin MacLeod\n"
                       "Link: https://incompetech.filmmusic.io/song/3952-killers\nLicense: "
                       "http://creativecommons.org/licenses/by/4.0/\n\n'The Path of the Goblin King' by Kevin MacLeod"
                       "\nLink: https://incompetech.filmmusic.io/song/4503-the-path-of-the-goblin-king\nLicense: "
                       "http://creativecommons.org/licenses/by/4.0/\n")

# OTHER STATES
pause = states.Pause()
yes_no = states.Yes_No()

# TODO :

# view_stats = """Allows the player to view their stats

# shop_weapons = Allows the user to choose a weapon to buy or nothing
# Prompt the user to type the exact name of what they want (i.e. "Scythe", "Scissors"... or "Exit)
# Force answer.capitalize()
# if answer =! 'Exit' or answer not in shop_stock, prompt again
# if exit, exit loop, else get shop_stock[answer]

# shop_spells =

# shop_armours =

# sell_items =


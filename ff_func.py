"""Fantasy Fight Project

-- Version 0.1
Author : Sophie Blanchard
Purpose : simple fight game with fantasy characters
Start date : 03-17-2020
Last update : 04-13-2020

This file contains some specific short functions used in the main program.
These functions must not need to import any other ff module.
"""

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
    print("~~~Fighting tips~~~\nBefore entering a fight, know that :\n- you may face one or more enemies depending "
          "on your level\n- you may cause damage to your enemy with your weapon (the more strong you are, the more "
          "damage you do),\n with your spell (the more clever you are, the more damage you do),\n or with your ability "
          "(this one is tricky : it can make a lot of damage but has also a more important fail risk.)\n- there is "
          "always a chance that your blow (or your adversary's) might fail.\n")
    print("~~~Ending game~~~\nYou may quit the game at any time.\nCaution ! This game does NOT save your character "
          "or your stats. It is a one-shot game !\nGood luck, and have fun !")

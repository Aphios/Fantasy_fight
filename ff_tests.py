"""Fantasy Fight Project

-- Version 0.1
Author : Sophie Blanchard
Purpose : simple fight game with fantasy characters
Start date : 03-17-2020
Last update : 03-18-2020

This file is used to test parts of the program or elements in the sub files.
"""
import ff_classes as ffc
import ff_func as fff

# Test Character creation and accessing attributes

settings = fff.autogen()
enemy = ffc.Character(**settings)

print(enemy.name, enemy.gender, enemy.race, enemy.level, enemy.ability)
print(enemy.armour, enemy.life, enemy.strength, enemy.protection, enemy.weapon, enemy.spell, enemy.intelligence)

# Test modifying attributes

enemy.life += 10
enemy.armour  = 'Rags'
enemy.protection = 0

print(enemy.life, enemy.armour, enemy.protection)
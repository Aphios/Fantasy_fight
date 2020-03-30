"""Fantasy Fight Project

-- Version 0.1
Author : Sophie Blanchard
Purpose : simple fight game with fantasy characters
Start date : 03-17-2020
Last update : 03-30-2020

This file is used to test the classes and their instances.
Tests to be runned with Pytest.
"""
import pytest
import ff_classes as ffc

# Test values
corset = ffc.Armour('Corset', 100, 5)
underwear = ffc.Armour('Underwear', 0, 0)
blizzard = ffc.Spell('Blizzard', 200, 8, 16)
no_spell = ffc.Spell('No spell', 0, 0, 0)
dagger = ffc.Weapon('Dagger', 150, 15, 25)
fists = ffc.Weapon('Fists', 0, -8, 4)


@pytest.fixture
def hero():
    """Returns a hero, aka Player."""
    return ffc.Player('Aphios', 'other', 'Banshee', underwear, fists, no_spell)


@pytest.fixture
def monster():
    """Returns a monster, aka a Character, enemy for Player"""
    return ffc.Character('Boss', 'Other', 'Tieflin', corset, dagger, no_spell, 5)


@pytest.fixture
def small_shop():
    """Returns a shop containing one armour object, one weapon object, one spell object"""
    return ffc.Shop({corset}, {dagger}, {blizzard})


# WEAPON
def test_weapon_get_price():
    assert dagger.price == 150


def test_weapon_get_damage_min():
    assert dagger.damage_min == 15


def test_weapon_set_price():
    dagger.price = 2
    assert dagger.price == 2


# ARMOUR
def test_armour_get_prot():
    assert corset.protection == 5


def test_armour_set_prot():
    corset.protection -= 1
    assert corset.protection == 4


# SPELL
def test_spell_get_damage_max():
    assert blizzard.damage_max == 16


def test_spell_set_damage_max():
    blizzard.damage_max += 4
    assert blizzard.damage_max == 20


# SHOP
def test_get_stock_armour(small_shop):
    assert small_shop.stock_armour == {corset}


def test_set_stock_armour(small_shop):
    small_shop.stock_armour.add(underwear)
    assert underwear in small_shop.stock_armourspell and corset in small_shop.stock_armour


def test_display_stock_armour(small_shop):
    d = small_shop.display(small_shop.stock_armour)
    assert d == "Corset : protection : 5, price : 100\nUnderwear : protection : 0, price : 0"


def test_display_stock_with_wrong_arg(small_shop):
    with pytest.raises(NameError):
        small_shop.display(stock_weapon)


def test_buy_with_wrong_item_type(small_shop):
    with pytest.raises(NameError):
        small_shop.buy('Corset')


def test_buy_with_wrong_player_type(small_shop):
    with pytest.raises(NameError):
        small_shop.buy(corset, Ismael)


def test_buy_not_enough_gold(hero):
    hero.gold = 5
    small_shop.buy(blizzard, hero)
    assert blizzard not in hero.inventory and hero.gold == 5


def test_buy(hero):
    hero.gold = 200
    small_shop.buy(blizzard, hero)
    assert blizzard in hero.inventory and hero.gold == 0


# Sell raises assert exception with wrong args (item / player)
# Sell removes from inventory and adds to gold half object's value

# PLAYER
# Access player race
# Set player race => should not be possible
# Set player name => should not be possible
# Set player ability => should not be possible
# Access player level
# Set player level
# Access to armour
# Set armour
# Access to inventory
# Add to inventory
# Display inventory
# Remove from inventory
# Loot
# Gain xp with enough xp will launch level up
# Gain xp without enough xp will set experience
# Level up will set level
# Print achievements
# Print player (must be different from character)
# Repr player (must be different from character)

# CHARACTER
# Print character (must be different from player)
# Repr character (must be different from player)

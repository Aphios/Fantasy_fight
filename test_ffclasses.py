"""Fantasy Fight Project. A simple fight game with fantasy characters.

This file is used to test the classes and their instances.
Tests are runned with Pytest.
"""

__version__ = 0.1
__author__ = "Sophie Blanchard"
__status__ = "Prototype"
__start_date__ = "03-17-2020"
__last_update__ = "04-15-2020"

import pytest
import ff_classes as ffc
import io


# Test values
@pytest.fixture
def corset():
    """returns an armour object : corset"""
    return ffc.Armour('Corset', 100, 5)


@pytest.fixture
def underwear():
    """returns an armour object : underwear"""
    return ffc.Armour('Underwear', 0, 0)


@pytest.fixture
def blizzard():
    """returns a spell object : blizzard"""
    return ffc.Spell('Blizzard', 200, 8, 16)


@pytest.fixture
def no_spell():
    """returns a spell object : no spell"""
    return ffc.Spell('No spell', 0, 0, 0)


@pytest.fixture
def dagger():
    """returns a weapon object : dagger"""
    return ffc.Weapon('Dagger', 150, 15, 25)


@pytest.fixture
def fists():
    """returns a weapon object : fists"""
    return ffc.Weapon('Fists', 0, -8, 4)


@pytest.fixture
def hero(underwear, fists, no_spell):
    """Returns a hero : Banshee level 1.
    Stats : underwear, no spell, fists, life : 28, strength 8, intelligence 20, ability : Scream
    """
    return ffc.Player('Aphios', 'Other', 'Banshee', underwear, fists, no_spell)


@pytest.fixture
def monster(corset, dagger, no_spell):
    """Returns a monster : Tieflin level 9.
    Stats : corset, dagger, no spell, life : 55, strength : 38, intelligence : 28, ability : Sting whip
    """
    return ffc.Character('Boss', 'Other', 'Tieflin', corset, dagger, no_spell, 9)


@pytest.fixture
def small_shop(corset, dagger, blizzard):
    """Returns a shop containing one armour object, one weapon object, one spell object"""
    return ffc.Shop({'Corset': corset, 'Dagger': dagger, 'Blizzard': blizzard})


# WEAPON
def test_weapon_get_price(dagger):
    assert dagger.price == 150


def test_weapon_get_damage_min(dagger):
    assert dagger.damage_min == 15


def test_weapon_set_price(dagger):
    dagger.price = 2
    assert dagger.price == 2


# ARMOUR
def test_armour_get_prot(corset):
    assert corset.protection == 5


def test_armour_set_prot(corset):
    corset.protection -= 1
    assert corset.protection == 4


# SPELL
def test_spell_get_damage_max(blizzard):
    assert blizzard.damage_max == 16


def test_spell_set_damage_max(blizzard):
    blizzard.damage_max += 4
    assert blizzard.damage_max == 20


# SHOP
def test_get_stock(small_shop):
    assert 'Corset' in small_shop.stock
    assert 'Dagger' in small_shop.stock
    assert 'Blizzard' in small_shop.stock


def test_set_and_display_stock(capsys, small_shop, underwear):
    small_shop.stock['Underwear'] = underwear
    small_shop.display()
    d = capsys.readouterr()
    assert "Corset : protection : 5, price : 100" in d.out and "Underwear : protection : 0, price : 0" in d.out


def test_buy_with_wrong_item_type(small_shop, hero, corset):
    with pytest.raises(AssertionError):
        hero.buy(corset, small_shop)


def test_buy_with_wrong_player_type(small_shop, monster):
    with pytest.raises(AttributeError):
        monster.buy('Corset', small_shop)


def test_buy_not_enough_gold(hero, small_shop):
    hero.gold = 5
    hero.buy('Blizzard', small_shop)
    assert 'Blizzard' not in hero.inventory and hero.gold == 5


def test_buy(hero, small_shop, blizzard):
    hero.gold = 200
    hero.buy('Blizzard', small_shop)
    assert 'Blizzard' in hero.inventory and blizzard in hero.inventory.values()
    assert hero.gold == 0


def test_sell_with_wrong_item_type(hero, underwear):
    with pytest.raises(AssertionError):
        hero.sell(underwear)


def test_sell_with_wrong_player_type(monster):
    with pytest.raises(AttributeError):
        monster.sell('Corset')


def test_sell(hero, corset):
    hero.inventory['Corset'] = corset
    hero.gold = 0
    hero.sell('Corset')
    assert corset not in hero.inventory.values() and hero.gold == 50


# PLAYER
def test_get_player_race(hero):
    assert hero._race == 'Banshee'


def test_get_player_life(hero):
    assert hero.life == 28


def test_get_character_life_with_high_level_on_init(monster):
    assert monster.life == 55


def test_set_player_life(hero):
    hero.life -= 10
    assert hero.life == 18


def test_set_player_level(hero):
    hero.level += 1
    assert hero.level == 2


def test_get_player_armour(hero):
    assert hero.armour.name == 'Underwear'


def test_set_player_armour(hero, corset):
    hero.armour = corset
    assert hero.armour.name == 'Corset'


def test_set_player_armour_wrong_operand(hero, corset):
    with pytest.raises(TypeError):
        hero.armour += corset


def test_display_inventory(capsys, hero, dagger):
    hero.gold = 5
    hero.inventory['Dagger'] = dagger
    hero.display_inventory()
    i = capsys.readouterr()
    assert i.out == ">>>>Aphios's inventory<<<<\nGold : 5\nDagger : min.damage : 15, max. damage : 25\n"


def test_loot(hero):
    g = hero.gold
    hero.loot()
    assert hero.gold >= g


def test_gain_xp_and_2_levels_up(hero, monster):
    print(hero)
    hero.gain_xp(monster)
    hero.gain_xp(monster)
    assert hero.level == 3
    assert hero.experience == 1500
    assert hero.life == 30


def test_achievements(capsys, hero):
    hero.wins += 3
    hero.achievements()
    a = capsys.readouterr()
    assert a.out == ">>>>> Aphios's achievements <<<<<\n3 enemies defeated. Last level reached : 1\n"


def test_display_player(hero):
    p = str(hero)
    assert p == "Name : Aphios\nGender : Other\nRace : Banshee\nLevel : 1\nStrength : 8\nIntelligence : 20\n" \
                "Life : 28\nSpecial Ability : Scream\n>>>>Equipment<<<<\nArmour : Underwear (protection : 0)\n" \
                "Weapon : Fists (min.damage : -8, max. damage : 4)\nSpell : No spell (min.damage : 0, " \
                "max. damage : 0\n>>>>Experience<<<<\n0 points. Next level in : 500 points."


def test_no_available_items(hero):
    assert hero.available_items() == []


def test_available_items(hero, corset):
    hero.inventory['Corset'] = corset
    assert hero.available_items() == ['Corset', 'Nothing']


def test_win(hero, monster):
    monster.life = -2
    assert hero.win_or_loose(monster)


def test_loose(hero, monster):
    hero.life = 0
    assert not hero.win_or_loose(monster)


# FIGHT
def test_equip_with_wrong_arg_type(hero, dagger):
    with pytest.raises(KeyError):
        hero.equip(dagger)


def test_equip(hero, dagger):
    hero.inventory['Dagger'] = dagger
    hero.equip('Dagger')
    assert hero.weapon == dagger
    assert 'Fists' in hero.inventory


def test_character_random_attack(monster):
    a = monster.random_attack()
    assert a == 'Sting whip' or a == 'Dagger'


def test_player_choose_attack(monkeypatch, hero):
    monkeypatch.setattr('sys.stdin', io.StringIO('Scream\n'))
    assert hero.choose_attack() == 'Scream'


def test_character_hit_diminished_by_armour(monkeypatch, monster, hero, corset):
    hero.armour = corset  # armour points 5
    monkeypatch.setattr('random.randint', lambda a, b: 10)  # damage 10 + 9 strength bonus
    monster.hit(hero, 'Dagger')  # total result : 28 - ((10 + 9) - 5)
    assert hero.life == 14


def test_player_hit_missed(monkeypatch, monster, hero):
    monkeypatch.setattr('random.randint', lambda a, b: -3)
    hero.hit(monster, 'Scream')
    assert monster.life == 55


def test_player_hit_desc(capsys, monkeypatch, monster, hero):
    monkeypatch.setattr('random.randint', lambda a, b: 20)
    hero.hit(monster, 'Scream')
    h = capsys.readouterr()
    assert h.out == "Aphios uses scream to attack !\n20 damage points dealt !\nBoss's armour absorbs 5 damage points." \
                    "\nBoss's life points are now 40.\n"

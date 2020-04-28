"""Fantasy Fight Project. A simple fight game with fantasy characters.

This file contains the classes :
- GameScene and its subclasses
"""

__version__ = 0.2
__author__ = "Sophie Blanchard"
__status__ = "Prototype"
__start_date__ = "03-17-2020"
__last_update__ = "04-28-2020"

import pygame
import gui_elements as gui

pygame.init()


class Game:
    """A master-class to contain each game scene (just as in theater scenes)."""

    def __init__(self):
        self.window = pygame.display.set_mode(ffc.RESOLUTION)
        self.continue_button = gui.Button('Continue', ffc.BLACK, ffc.BURGUNDY, ffc.IMMORTAL_BIG)
        self.yes_button = gui.Button('Yes', ffc.BLACK, ffc.NAVY, ffc.IMMORTAL_BIG)
        self.no_button = gui.Button('No', ffc.BLACK, ffc.NAVY, ffc.IMMORTAL_BIG)
        self.clock = pygame.time.Clock()
        self.logo = pygame.image.load('Images/FF_logo.png').convert_alpha()
        pygame.display.set_caption("Fantasy Fight")
        pygame.display.set_icon(self.logo)

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

    def blit_text(self, text, position, font, color):
        """Blits hashed text in the window, respecting newlines.

        Args : position : a tuple / font : font object / color : color object / text : string
        / surface : surface object.
        Rendering is anti-aliased.
        """
        words = [word.split(' ') for word in text.splitlines()]
        space = font.size(' ')[0]  # The width of a space.
        max_width, max_height = self.window.get_size()
        x, y = position
        for line in words:
            for word in line:
                word_surface = font.render(word, True, color)
                word_width, word_height = word_surface.get_size()
                if x + word_width >= max_width:
                    x = position[0]  # Reset the x.
                    y += word_height  # Start on new row.
                self.window.blit(word_surface, (x, y))
                x += word_width + space
            x = position[0]  # Reset the x.
            y += word_height  # Start on new row.

    def text_buttons(self, color_surf, font, color_font, text, pos_text, button_1, pos_button_1,
                     button_2=None, pos_button_2=None):
        """Blits texts on a colored Surface, with one or two buttons."""
        self.window.fill(color_surf)
        self.blit_text(text, pos_text, font, color_font)
        button_1.blit_button(self.window, pos_button_1)
        if button_2:
            button_2.blit_button(self.window, pos_button_2)
        pygame.display.flip()

    def update(self):
        pass


class GameTitle(Game):
    """First game scene + music.

     The introduction screen with the game's title.
     """

    def update(self):
        """Loads intro music and Plays intro music and renders intro screen"""
        pygame.mixer_music.set_volume(0.50)
        pygame.mixer_music.load("Music/the-descent.mp3")
        pygame.mixer_music.play(-1)
        intro_screen = pygame.image.load('Images/Fantasy_fight.png').convert_alpha()
        self.window.blit(intro_screen, (0, 0))
        self.blit_text("Fantasy Fight\n", (280, 270), ffc.IMMORTAL_BIG, ffc.BLACK)
        pygame.display.flip()
        time.sleep(2)


class GameStory(Game):
    """Displays the story of the game."""

    def update(self):
        self.text_buttons(ffc.VIOLET, ffc.IMMORTAL_SMALL, ffc.BLACK, "Fantasy Fight is a basic "
                          "'read and choose' game.\n~~~STORY~~~\nYou enter the Forgotten Realms, a fantasy world "
                          "where heroes fight for power and glory.\n~~~GOAL~~~\nYour goal is to defeat as many "
                          "enemies as you can and gain eternal renoun !", (10, 50), self.continue_button, (400, 500))


class GameRules(Game):
    """Displays the game rules."""

    def update(self):
        self.text_buttons(ffc.VIOLET, ffc.IMMORTAL_SMALL, ffc.BLACK, "~~~RULES~~~\nYou will create a "
                          "character and be given some money (or not if you're unlucky !) to buy some "
                          "equipment.\nYou can choose to be a Rakshasa, an Illithid, a Tieflin, a Banshee or a "
                          "Githzerai.\nFrom your race depends your life force, your strength, your intelligence and "
                          "your special ability.\nYou will be able to buy weapons, armours and spells. You can also "
                          "sell equipment in your inventory.\nYou cannot sell your current weapon, spell or armour "
                          "unless you equip something else.\nThen you will fight other characters "
                          "until you die or choose to retire.\nEach enemy defeated is rewarded by experience points "
                          "and a chance to loot some gold.\nWhen you have earned enough experience, you will gain a "
                          "level and your stats will increase.\n", (10, 50), frame.continue_button, (400, 500))


class GameTips(Game):
    """Displays the game tips."""

    def update(self):
        self.text_buttons(ffc.VIOLET, ffc.IMMORTAL_SMALL, ffc.BLACK, "~~~Fighting tips~~~\nBefore "
                          "entering a fight, know that :\n- you may cause damage to your enemy with your "
                          "weapon (the more strong you are, the more damage you do),\n with your spell (the more clever"
                          "you are, the more damage you do),\n or with your ability (this one is tricky : it can make "
                          "a lot of damage but has also a more important fail risk.)\n- there is always a chance "
                          "that your blow (or your adversary's) might fail.\n~~~Ending game~~~\nYou may quit the "
                          "game at any time.\nCaution ! This game does NOT save your character or your stats. It is"
                          " a one-shot game !\nGood luck, and have fun !", (10, 50), frame.continue_button, (400, 500))


class GameOver(Game):
    """Displays the game over message and credits."""

    def update(self):
        self.blit_text("~~~Game over~~~\nThank you for playing !\n~~~CREDITS~~~\nConception & "
                       "programming : Aphios\nMusic:\n'The Descent' by Kevin MacLeod\nLink: "
                       "https://incompetech.filmmusic.io/song/4490-the-descent\nLicense: "
                       "http://creativecommons.org/licenses/by/4.0/\n'Crossing the Chasm' by Kevin MacLeod\n"
                       "Link: https://incompetech.filmmusic.io/song/3562-crossing-the-chasm\nLicense: "
                       "http://creativecommons.org/licenses/by/4.0/\n'Killers' by Kevin MacLeod\n"
                       "Link: https://incompetech.filmmusic.io/song/3952-killers\nLicense: "
                       "http://creativecommons.org/licenses/by/4.0/\n'The Path of the Goblin King' by Kevin MacLeod"
                       "Link: https://incompetech.filmmusic.io/song/4503-the-path-of-the-goblin-king\nLicense: "
                       "http://creativecommons.org/licenses/by/4.0/\n", (10, 500), ffc.IMMORTAL_SMALL, ffc.BLACK)
        time.sleep(20)


class Pause(Game):
    """Freezes the game until the continue button is hit."""

    def handle_events(self):
        pause = True
        while pause:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
                if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                    if self.continue_button.box.collidepoint(event.pos):
                        return


class Yes_No(Game):
    """Freezes the game until the YES or the NO button is hit."""

    def handle_events(self):
        wait = True
        while wait:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
                # TODO hit button 1 or button 2

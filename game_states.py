"""Fantasy Fight Project. A simple fight game with fantasy characters.

This file contains classes handling the game states, such as the main game structure, intro, end, pause, etc.
"""

__version__ = 0.2
__author__ = "Sophie Blanchard"
__status__ = "Prototype"
__start_date__ = "03-17-2020"
__last_update__ = "05-02-2020"

import pygame
import time
import constants as cst
import gui_elements as gui

pygame.init()

class Game:
    """A master-class to contain each game scene (just as in theater scenes)."""

    def __init__(self, *args, **kwargs):
        self.window = pygame.display.set_mode(cst.RESOLUTION)
        self.continue_button = gui.Button('Continue', cst.BLACK, cst.GOLD, cst.IMMORTAL_BIG, (400, 550))
        self.yes_button = gui.Button('Yes', cst.BLACK, cst.GOLD, cst.IMMORTAL_BIG, (350, 550))
        self.no_button = gui.Button('No', cst.BLACK, cst.BURGUNDY, cst.IMMORTAL_BIG, (450, 550))
        self.clock = pygame.time.Clock()
        self.logo = pygame.image.load('Images/FF_logo.png').convert_alpha()
        self.screen = pygame.image.load('Images/Fantasy_fight.png').convert_alpha()
        self.bg = pygame.image.load('Images/Fantasy_fight_bg.png').convert_alpha()
        self.font_big = cst.IMMORTAL_BIG
        self.font_small = cst.IMMORTAL_SMALL
        self.input_box = gui.InputBox(250, 500, 300, 35)
        pygame.display.set_caption("Fantasy Fight")
        pygame.display.set_icon(self.logo)

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

    def blit_text(self, text, position, font, font_color):
        """Blits hashed text, respecting newlines.

        Args : position : a tuple / font : font object / font_color : color object / text : string
        / surface : surface object.
        Rendering is anti-aliased.
        """
        words = [word.split(' ') for word in text.splitlines()]
        space = font.size(' ')[0]  # The width of a space.
        max_width, max_height = self.window.get_size()
        x, y = position
        for line in words:
            for word in line:
                word_surface = font.render(word, True, font_color)
                word_width, word_height = word_surface.get_size()
                if x + word_width >= max_width:
                    x = position[0]  # Reset the x.
                    y += word_height  # Start on new row.
                self.window.blit(word_surface, (x, y))
                x += word_width + space
            x = position[0]  # Reset the x.
            y += word_height  # Start on new row.

    def text_continue(self, font, color_font, text, pos_text):
        """Blits text on the colored Surface + continue button.

        Args : pos_text : tuple of x, y coordinates of font rectangle
        pos_button : tuple of x, y coordinates of center of the button.
        """
        self.blit_text(text, pos_text, font, color_font)
        self.continue_button.blit_button(self.window)

    def text_yesno(self, font, color_font, text, pos_text):
        """Blits text on the colored Surface + yes and no buttons.

        Args : pos_text : tuple of x, y coordinates of font rectangle
        pos_yes and pos_no : tuples of x, y coordinates of center of the buttons.
        """
        self.blit_text(text, pos_text, font, color_font)
        self.yes_button.blit_button(self.window)
        self.no_button.blit_button(self.window)

    def run(self, *args, **kwargs):
        pygame.display.flip()

    def get_ui(self):
        """Retrieves an user input from a text box."""

        ui = ''
        while not ui:
            ui = self.input_box.handle_events()
            self.input_box.blit_txtbox(self.window)
            pygame.display.flip()
            self.clock.tick()
        return ui.capitalize()


class GameScene(Game):
    """A scene from the game."""

    def __init__(self, text='', music=None, *args, **kwargs):
        Game.__init__(self, *args, **kwargs)
        self.text = text
        self.music = music

    def play_music(self, repeats):
        """Loads and plays a music for a certain number of repetitions."""

        pygame.mixer_music.set_volume(0.50)
        pygame.mixer_music.load(self.music)
        pygame.mixer_music.play(repeats)

    def stop_music(self, fade_time):
        """Stops the current music with fadeout."""
        pygame.mixer_music.fadeout(fade_time)
        self.clock.tick(cst.FPS)

    def display_text(self, position=(10, 20), font=cst.IMMORTAL_SMALL):
        """Displays some text onto the screen."""

        self.blit_text(self.text, position, font, cst.BLACK)
        pygame.display.flip()

    def display_text_continue(self, position=(10,20)):
        """Displays some text onto the screen with a continue button."""

        self.text_continue(self.font_small, cst.BLACK, self.text, position)
        pygame.display.flip()

    def display_text_yesno(self, position=(10,20)):
        """Displays some text onto the screen with yes and no buttons."""

        self.text_yesno(self.font_small, cst.BLACK, self.text, position)
        pygame.display.flip()

    def ask_user(self, position=(10,150)):
        """Displays some text and a input box below to retrieve player's input."""

        self.blit_text(self.text, position, self.font_small, cst.BLACK)
        self.input_box.blit_txtbox(self.window)
        pygame.display.flip()


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
                        pause = False


class Yes_No(Game):
    """Freezes the game until the YES or the NO button is hit."""

    def handle_events(self):
        wait = True
        while wait:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
                elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                    if self.yes_button.box.collidepoint(event.pos):
                        return True
                    elif self.no_button.box.collidepoint(event.pos):
                        return False




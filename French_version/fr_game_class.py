"""Fantasy Fight Project. A simple fight game with fantasy characters.

This file contains the class handling the game states, such as the main game functions, intro, end, pause, etc.
"""

__version__ = 0.3
__author__ = "Sophie Blanchard"
__start_date__ = "03-17-2020"
__last_update__ = "05-13-2020"

import random
import time

import pygame

import French_version.fr_constants as cst
import French_version.fr_gui_elements as gui

pygame.init()


class Game:
    """A master-class to contain each game scene (just as in theater scenes)."""

    def __init__(self, *args, **kwargs):
        self.window = pygame.display.set_mode(cst.RESOLUTION)
        self.continue_button = gui.Button('Continuer', cst.BLACK, cst.GOLD, cst.IMMORTAL_BIG, (400, 550))
        self.yes_button = gui.Button('Oui', cst.BLACK, cst.GOLD, cst.IMMORTAL_BIG, (350, 550))
        self.no_button = gui.Button('Non', cst.BLACK, cst.BURGUNDY, cst.IMMORTAL_BIG, (450, 550))
        self.clock = pygame.time.Clock()
        self.logo = pygame.image.load('Images/FF_logo.png').convert_alpha()
        self.screen = pygame.image.load('Images/Fantasy_fight.png').convert_alpha()
        self.img_shop = pygame.image.load('Images/shop1.jpg').convert_alpha()
        self.img_arena = pygame.image.load('Images/arena2.JPG').convert_alpha()
        self.bg = pygame.image.load('Images/Fantasy_fight_bg.png').convert_alpha()
        self.large_pane = pygame.image.load('Images/large_pane.png').convert_alpha()
        self.pane = pygame.image.load('Images/medium_pane.png').convert_alpha()
        self.font_big = cst.IMMORTAL_BIG
        self.font_small = cst.IMMORTAL_SMALL
        self.input_box = gui.InputBox(250, 500, 300, 35)
        self.intro_music = "Music/the-descent.mp3"
        self.fight_music1 = "Music/crossing-the-chasm.mp3"
        self.fight_music2 = "Music/killers.mp3"
        self.shop_music = "Music/the-path-of-the-goblin-king.mp3"
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

    def get_ui(self):
        """Retrieves an user input from a text box."""

        ui = ''
        while not ui:
            ui = self.input_box.handle_events()
            self.input_box.blit_txtbox(self.window)
            pygame.display.flip()
            self.clock.tick()
        return ui.capitalize()

    def play_random_music(self, repeats=-1):
        """Loads and plays a random music for a certain number of repetitions."""

        music = random.choice([self.fight_music1, self.fight_music2])
        pygame.mixer_music.set_volume(0.30)
        pygame.mixer_music.load(music)
        pygame.mixer_music.play(repeats)

    def play_music(self, music, repeats=-1):
        """Loads and plays a music for a certain number of repetitions."""

        pygame.mixer_music.set_volume(0.30)
        pygame.mixer_music.load(music)
        pygame.mixer_music.play(repeats)

    def stop_music(self, fade_time):
        """Stops the current music with fadeout."""

        pygame.mixer_music.fadeout(fade_time)
        self.clock.tick(cst.FPS)

    def pause(self):
        """Handles events when the game is paused with a continue button."""

        pause = True
        while pause:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
                if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                    if self.continue_button.box.collidepoint(event.pos):
                        pause = False

    def yes_no(self):
        """Handles events when the game waits for the user to click to 'yes' or 'no' button."""

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

    def verify_ui(self, inpt, accepted_terms):
        """Checks if the user input corresponds to one of the accepted terms.

        Args : accepted_terms must be a sequence of capitalized strings, e.g. ['Scythe', 'Scissors']...
        """

        if inpt not in accepted_terms:
            return False
        else:
            return True

    def text_music_sleep(self, text, sleep_time, back_surf, pos_txt=(20, 30), music=None, rpt_music=-1,
                         font=cst.IMMORTAL_SMALL, font_color=cst.BLACK, subtext=None, subpos=(110, 215)):
        """Plays a music, blits the back surface with a text, then makes the program sleep.

        May blit text on an image surface if subtext is passed in argument.
        """

        self.handle_events()
        if music is not None:
            self.play_music(music, rpt_music)
        self.window.blit(back_surf, (0, 0))
        if subtext:
            self.window.blit(subtext, subpos)
        self.blit_text(text, pos_txt, font, font_color)
        pygame.display.flip()
        time.sleep(sleep_time)
        self.clock.tick(cst.FPS)

    def text_img_continue(self, text, back_surf, pos=(20, 30), button_color=cst.GOLD,
                          font=cst.IMMORTAL_SMALL, font_color=cst.BLACK, subtext=None, subpos=(110, 215),
                          picture=None, pos_picture=(100, 400), picture2=None, pos_picture2=(650, 400)):
        """Displays a background, a text and a continue button and handles the pause system.

        Options : Blits a back image (e.g. text pane) given subtext (image) and subpos (tuple).
        Blits one or two pictures (e.g. character pictures) given picture (image) and pos_picture (tuple).
        """

        self.handle_events()
        self.window.blit(back_surf, (0, 0))
        if subtext:
            self.window.blit(subtext, subpos)
        if picture:
            pic = pygame.image.load(picture).convert_alpha()
            pict = pygame.transform.scale2x(pic)
            self.window.blit(pict, pos_picture)
        if picture2:
            pic2 = pygame.image.load(picture2).convert_alpha()
            pict2 = pygame.transform.scale2x(pic2)
            self.window.blit(pict2, pos_picture2)
        self.blit_text(text, pos, font, font_color)
        self.continue_button.blit_button(self.window, button_color)
        pygame.display.flip()
        self.clock.tick(cst.FPS)
        self.pause()

    def ask_check_img(self, question, back_surf, accepted, pos_question=(40, 170), font=cst.IMMORTAL_SMALL,
                      font_color=cst.BLACK, subtext=None, subpos=(110, 215), picture=None, pos_picture=(100, 400),
                      picture2=None, pos_picture2=(650, 400)):
        """A loop to verify user input.

        Options : Blits a back image (i.e. text pane) given subtext (image) and subpos (tuple).
        Blits one or two pictures (i.e. character pictures) given picture (image) and pos_picture (tuple).
        """

        self.input_box.clear()
        var = ''
        while not self.verify_ui(var, accepted):
            self.handle_events()
            self.window.blit(back_surf, (0, 0))
            if subtext:
                self.window.blit(subtext, subpos)
            if picture:
                pic = pygame.image.load(picture).convert_alpha()
                pict = pygame.transform.scale2x(pic)
                self.window.blit(pict, pos_picture)
            if picture2:
                pic2 = pygame.image.load(picture2).convert_alpha()
                pict2 = pygame.transform.scale2x(pic2)
                self.window.blit(pict2, pos_picture2)
            self.blit_text(question, pos_question, font, font_color)
            self.input_box.blit_txtbox(self.window)
            pygame.display.flip()
            var = self.get_ui()
        return var

    def ask_user(self, question, back_surf, pos_question=(20, 150), font=cst.IMMORTAL_SMALL,
                 font_color=cst.BLACK, subtext=None, subpos=(110, 215)):
        """Asks a question to the user and retrieves the input without checking it.

        Default background is displayed + a question to the player + the input box.
        May blit text on a white rect if a Rect object is passed in argument.
        """

        self.input_box.clear()
        self.handle_events()
        self.window.blit(back_surf, (0, 0))
        if subtext:
            self.window.blit(subtext, subpos)
        self.blit_text(question, pos_question, font, font_color)
        self.input_box.blit_txtbox(self.window)
        pygame.display.flip()
        answer = self.get_ui()
        return answer

    def text_wait(self, text, back_surf, pos=(20, 30), wait=0, font=cst.IMMORTAL_SMALL,
                  font_color=cst.BLACK, subtext=None, subpos=(110, 215)):
        """Displays scene.text at default position (10, 20) on the background with default font.

        May blit text on a white rect if a Rect object is passed in argument.
        """

        self.handle_events()
        self.window.blit(back_surf, (0, 0))
        if subtext:
            self.window.blit(subtext, subpos)
        self.blit_text(text, pos, font, font_color)
        pygame.display.flip()
        if wait:
            time.sleep(wait)
        self.clock.tick(cst.FPS)

    def text_yesno(self, text, back_surf, pos_txt=(20, 300), font=cst.IMMORTAL_SMALL, font_color=cst.BLACK,
                   subtext=None, subpos=(110, 215)):
        """ Blits text on the background and the yes/no buttons, then returns the user's answer (True or False).

        May blit text on a white rect if a Rect object is passed in argument.
        """

        self.handle_events()
        self.window.blit(back_surf, (0, 0))
        if subtext:
            self.window.blit(subtext, subpos)
        self.blit_text(text, pos_txt, font, font_color)
        self.yes_button.blit_button(self.window)
        self.no_button.blit_button(self.window)
        pygame.display.flip()
        self.clock.tick(cst.FPS)
        return self.yes_no()

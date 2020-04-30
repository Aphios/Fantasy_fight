"""Fantasy Fight Project. A simple fight game with fantasy characters.

This file contains the classes :
- Button
"""

__version__ = 0.2
__author__ = "Sophie Blanchard"
__status__ = "Prototype"
__start_date__ = "03-17-2020"
__last_update__ = "04-30-2020"

import pygame
import constants as cst

pygame.init()


class Button:
    """A button with a text."""

    def __init__(self, text, text_color, bg_color, font, pos):
        self.msg = font.render(text, True, text_color, bg_color)
        self.pos = pos
        self.box = self.msg.get_rect(center=self.pos)

    def blit_button(self, surf, color=(255, 255, 255)):
        """Blits a rectangular button onto the Surface at coordinates x, y.
        Args : surf : the Surface / center : a tuple with coordinates of the center of the button / color : default
        is white.
        """

        pygame.draw.rect(surf, color, self.box)
        surf.blit(self.msg, self.box)


class InputBox:
    """A input box taking input from the user and displaying it.

    Features a maximum length of characters.
    """

    def __init__(self, x, y, w, h, max_len=20):
        self.rect = pygame.Rect(x, y, w, h)
        self.txt_color = cst.BLACK
        self.bg_color = cst.WHITE
        self.text = ''
        self.max_len = max_len
        self.txt_surface = cst.IMMORTAL_SMALL.render(self.text, True, self.txt_color, self.bg_color)

    def handle_events(self):
        """Displays the text entered in the box if a key is pressed."""

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    return self.text
                elif event.key == pygame.K_BACKSPACE:
                    self.text = self.text[:-1]
                else:
                    if len(self.text) < self.max_len:
                        self.text += event.unicode

    def blit_txtbox(self, screen):
        """Displays the text box with its content."""

        # Render the text.
        self.txt_surface = cst.IMMORTAL_SMALL.render(self.text, True, self.txt_color, self.bg_color)
        # Blit the rect.
        pygame.draw.rect(screen, self.bg_color, self.rect)
        # Blit the text.
        screen.blit(self.txt_surface, (self.rect.x + 5, self.rect.y + 5))
        pygame.display.update()

    def clear(self):
        """After the box has been used, it is necessary to clear it for further use."""

        self.text = ''


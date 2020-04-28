"""Fantasy Fight Project. A simple fight game with fantasy characters.

This file contains the classes :
- Button
"""

__version__ = 0.2
__author__ = "Sophie Blanchard"
__status__ = "Prototype"
__start_date__ = "03-17-2020"
__last_update__ = "04-28-2020"

import pygame

pygame.init()


class Button:
    """A button with a text."""

    def __init__(self, text, text_color, bg_color, font):
        self.msg = font.render(text, True, text_color, bg_color)
        self.box = self.msg.get_rect()

    def blit_button(self, surf, center):
        """Blits the button onto the Surface at coordinates x, y."""
        self.box.center = center
        surf.blit(self.msg, self.box)
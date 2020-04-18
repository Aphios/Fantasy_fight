"""Fantasy Fight Project. A simple fight game with fantasy characters.

This file contains the base GUI frame made with pygame.
"""

__version__ = 0.2
__author__ = "Sophie Blanchard"
__status__ = "Prototype"
__start_date__ = "03-17-2020"
__last_update__ = "04-18-2020"

import pygame

pygame.init()

# CONSTANTS
# Colors
RESOLUTION = (640, 480)
VIOLET = (89, 33, 129)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREY = (105, 95, 110)
NAVY = (7, 53, 179)
BURGUNDY = (122, 15, 36)
# Animation
FPS = 30

# Window creation
window = pygame.display.set_mode(RESOLUTION)
pygame.display.set_caption("Fantasy Fight")

# Clock creation
clock = pygame.time.Clock()

# Images (to convert) : TODO

# Sounds : TODO

# Musics : TODO

# >>> Game loop <<<
launched = True
while launched:
    window.fill(VIOLET)

    # Intro phases (play 'The descent')
    # Paste cover image
    # Shop and equip phases (play 'The path of the goblin king')
    # Fight phase (play randomly 'Killers' or 'Crossing the chasm')
    # End game (play 'The descent')

    for event in pygame.event.get():
        if event.type is pygame.QUIT:
            launched = False

    pygame.display.update()
    clock.tick(FPS)
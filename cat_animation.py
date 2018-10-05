# https://www.youtube.com/watch?v=g7KoOUu4v7Q - followed along with this video
# https://drive.google.com/drive/folders/0BwDJQBs1OukNOEtwNlBxUkVlcFk - images and scripts

import sys
import random
import math

import pygame
import pygame.gfxdraw
from pygame.locals import *

pygame.init()

CLOCK = pygame.time.Clock()

# SETUP CANVAS -------------------------------------------------------------------------------------------------------------
CANVAS_WIDTH = 1280
CANVAS_HEIGHT = 720
CW_HALF = CANVAS_WIDTH / 2
CH_HALF = CANVAS_HEIGHT / 2
DS = pygame.display.set_mode((CANVAS_WIDTH, CANVAS_HEIGHT))

# LOAD IMAGES USING LIST METHOD --------------------------------------------------------------------------------------------
CATS = list(
    [pygame.image.load('catwalk_{0}.png'.format(i)) for i in range(1, 13)])
# doing loop inside of list works because of list comprehension. ref: https://docs.python.org/3/tutorial/datastructures.html#list-comprehensions
# syntax is equal to:
# CATS = []
# for i in range(1, 13):
#     CATS.append(pygame.image.load('catwalk_{0}.png'.format(i)))

# SET VARIABLES ------------------------------------------------------------------------------------------------------------
RECT = CATS[0].get_rect()
FRAME_COUNT = 12


# FUNCTIONS ----------------------------------------------------------------------------------------------------------------
def event_handler():
    for event in pygame.event.get():
        if event.type == QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE):
            pygame.quit()
            sys.exit()


def sprite_animation():
    CAT = pygame.image.load('catwalk.png')
    RECT = CAT.get_rect()
    FRAME_HEIGHT = RECT.height / FRAME_COUNT
    FRAMES = list([(0, FRAME_HEIGHT * frame, RECT.width, FRAME_HEIGHT)
                   for frame in range(FRAME_COUNT)])
    DS.blit(CAT, (CW_HALF - RECT.center[0],
                  CH_HALF - FRAME_HEIGHT / 2), FRAMES[frame])


frame = 0
# EVENT LOOP ---------------------------------------------------------------------------------------------------------------
while True:
    event_handler()

    # list animation
    # DS.blit(CATS[frame], (CW_HALF - RECT.center[0], CH_HALF - RECT.center[1]))

    # sprite animation (partial image)
    sprite_animation()

    frame += 1
    if frame > FRAME_COUNT - 1:
        frame = 0

    pygame.display.update()

	#set global FPS
    CLOCK.tick(120)

    # set background color
    DS.fill((128, 128, 128))

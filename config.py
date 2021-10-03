import pygame as pg
import sprites

## GAME INIT ##

#SCRN_WIDTH, SCRN_HEIGHT = 640, 480
#WIN_WIDTH, WIN_HEIGHT = 1600, 900
#WIN_WIDTH, WIN_HEIGHT = 640, 480

WIN_WIDTH, WIN_HEIGHT = 640, 480
SCRN_WIDTH, SCRN_HEIGHT = 200, 160

MS = pg.Surface((SCRN_WIDTH, SCRN_HEIGHT)) # Main Screen
WIN = pg.display.set_mode((WIN_WIDTH, WIN_HEIGHT)) # Window

## INTRO SCREEN ##

INTRO_Y = 2
INTRO_TERRA_X = 5
INTRO_LOCKE_X = INTRO_TERRA_X + 2

## SPRITES CONF ##

TILESIZE = 16

SPRITE_WIDTH = 28
SPRITE_HEIGHT = 52

FPS = 60

BLOCK_LAYER = 1

PLAYER_LAYER = 6
PLAYER_SPEED = 2

RED = (255,0,0)
BLACK = (0,0,0)
BLUE = (0,0,255)

tilemap = [
           'BBBBBBBBBBBBBBBBBBBB',
           'B..................B',
           'B..................B',
           'B..................B',
           'B......BBB.........B',
           'B.........P........B',
           'B..................B',
           'B..................B',
           'B.......BBB........B',
           'B.........B........B',
           'B.........B........B',
           'B..................B',
           'B..................B',
           'B..................B',
           'BBBBBBBBBBBBBBBBBBBB',
]
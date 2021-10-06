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

INTRO_SCREEN_BOTTOM = 160

## SPRITES CONF ##

TILESIZE = 16

TERRA_ASSET = 'assets/terra/Terra.png'
LOCKE_ASSET = 'assets/locke/Locke.png'

SPRITE_WIDTH = 16
SPRITE_HEIGHT = 24

FPS = 60

BLOCK_LAYER = 1

OCEAN_X, OCEAN_Y = (6 * TILESIZE), (5 * TILESIZE)
OCEAN_WIDTH, OCEAN_HEIGHT = (10 * TILESIZE), (9 * TILESIZE)

PLAYER_LAYER = 6
PLAYER_SPEED = 2

MOVEMENT_FRAMES = int(TILESIZE / PLAYER_SPEED)

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
import pygame as pg
from config import *
import sys
import math
import random
import pytmx

class Spritesheet:
    def __init__(self, file):
        self.sheet = pg.image.load(file).convert()
    
    def get_sprite(self, x, y, width, height):
        sprite = pg.Surface([width, height])
        sprite.blit(self.sheet, (0,0), (x, y, width, height))
        sprite.set_colorkey(BLACK)
        return sprite

class Character(pg.sprite.Sprite):
    def __init__(self, spritesheet, game, x, y):
        self.game = game
        self._layer = 3
        self.groups = self.game.all_sprites
        pg.sprite.Sprite.__init__(self, self.groups)

        self.x = x * TILESIZE
        self.y = y * TILESIZE
        self.width = SPRITE_WIDTH
        self.height = SPRITE_HEIGHT

        # /-- TEMP
        self.x_change = 0
        self.y_change = 0
        # --/

        self.character_spritesheet = Spritesheet(spritesheet)

        self.FRONT = self.character_spritesheet.get_sprite(0, 0, 16, 24)
        self.LEFT = self.character_spritesheet.get_sprite(113, 0, 16, 24)
        self.RIGHT = pg.transform.flip(self.LEFT, True, False)
        self.BACK = self.character_spritesheet.get_sprite(65, 0, 16, 24)

        self.facing = 'FRONT'
        self.image = self.FRONT

        self.rect = self.image.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y
    
    def update(self):
        self.rect.x += self.x_change
        self.rect.y += self.y_change

        self.x_change = 0
        self.y_change = 0

class Player(Character):
    def __init__(self, spritesheet, game, x, y):
        super().__init__(spritesheet, game, x, y)

    def update(self):
        keys = pg.key.get_pressed()
        if keys[pg.K_ESCAPE]:
            pg.quit()
            sys.exit()
        
        if self.game.playing == True:
            self.movement()
            self.rect.x += self.x_change
            self.rect.y += self.y_change

            self.x_change = 0
            self.y_change = 0

    def movement(self):
        keys = pg.key.get_pressed()
        if keys[pg.K_a]:
            self.x_change -= PLAYER_SPEED
            self.y_change = 0
            if self.facing != 'LEFT':
                self.facing = 'LEFT'
                self.image = self.LEFT
        if keys[pg.K_d]:
            self.x_change += PLAYER_SPEED
            self.y_change = 0
            if self.facing != 'RIGHT':
                self.facing = 'RIGHT'
                self.image = self.RIGHT
        if keys[pg.K_w]:
            self.y_change -= PLAYER_SPEED
            self.x_change = 0
            if self.facing != 'BACK':
                self.facing = 'BACK'
                self.image = self.BACK
        if keys[pg.K_s]:
            self.y_change += PLAYER_SPEED
            self.x_change = 0
            if self.facing != 'FRONT':
                self.facing = 'FRONT'
                self.image = self.FRONT

class Block(pg.sprite.Sprite):
    def __init__(self,game, x, y):
        self.game = game
        self._layer = BLOCK_LAYER
        self.groups = self.game.all_sprites, self.game.blocks
        pg.sprite.Sprite.__init__(self, self.groups)

        self.x = x * TILESIZE
        self.y = y * TILESIZE
        self.width = TILESIZE
        self.height = TILESIZE

        self.image = pg.Surface([self.width, self.height])
        self.image.fill(BLUE)

        self.rect = self.image.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y

class Map:
    def __init__(self, filename):
        self.data = []
        with open(filename, 'rt') as f:
            for line in f:
                self.data.append(line.strip())

        self.tilewidth = len(self.data[0])
        self.tileheight = len(self.data)
        self.width = self.tilewidth * TILESIZE
        self.height = self.tileheight * TILESIZE

class TiledMap(pg.sprite.Sprite):
    def __init__(self, game, filename):
        self.game = game
        self.tmxdata = pytmx.load_pygame(filename, pixelalpha=True)
        self.width = self.tmxdata.width * self.tmxdata.tilewidth
        self.height = self.tmxdata.height * self.tmxdata.tileheight
        self.groups = self.game.blocks
        
    def make_map(self):
        temp_surface = pg.Surface((self.width, self.height))
        #self.render(temp_surface)
        return temp_surface
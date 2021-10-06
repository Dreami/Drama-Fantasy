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

class Ocean(pg.sprite.Sprite):
    def __init__(self, game):
        self.game = game
        self.layer = 2
        self.groups = self.game.all_sprites
        pg.sprite.Sprite.__init__(self, self.groups)
        self.x = OCEAN_X
        self.y = OCEAN_Y
        self.width = OCEAN_WIDTH
        self.height = OCEAN_HEIGHT

        self.ocean_sprite = Spritesheet('assets/solitary_island_water.png')
        animation = [self.ocean_sprite.get_sprite(84, 44, self.width, self.height),
                    self.ocean_sprite.get_sprite(352, 44, self.width, self.height), 
                    self.ocean_sprite.get_sprite(628, 44, self.width, self.height), 
                    self.ocean_sprite.get_sprite(628, 44, self.width, self.height),
                    self.ocean_sprite.get_sprite(905, 44, self.width, self.height),
                    self.ocean_sprite.get_sprite(1180, 44, self.width, self.height)]


class Character(pg.sprite.Sprite):
    def __init__(self, spritesheet, game, x, y):
        self.game = game
        self._layer = 1
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

        self.FRONT = self.character_spritesheet.get_sprite(16, 0, self.width, self.height)
        self.LEFT = self.character_spritesheet.get_sprite(113, 0, self.width, self.height)
        self.RIGHT = pg.transform.flip(self.LEFT, True, False)
        self.BACK = self.character_spritesheet.get_sprite(65, 0, self.width, self.height)

        self.facing = 'FRONT'
        self.image = self.FRONT

        self.rect = self.image.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y
    
    def update(self):
        self.rect.x += self.x_change
        self.rect.y += self.y_change

class Player(Character):
    def __init__(self, spritesheet, game, x, y):
        super().__init__(spritesheet, game, x, y)

    def update(self):
        keys = pg.key.get_pressed()
        
        self.movement(keys)
        self.rect.x += self.x_change
        self.rect.y += self.y_change
        
        if self.x_change != 0:
            while self.rect.x % TILESIZE != 0:
                self.rect.x += self.x_change
                self.game.draw()
        elif self.y_change != 0:
            while self.rect.y % TILESIZE != 0:
                self.rect.y += self.y_change
                self.game.draw()

        self.x_change = 0
        self.y_change = 0

    def movement(self, keys):
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
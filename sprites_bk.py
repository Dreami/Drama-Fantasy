import pygame as pg
from config import *
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

class Player(pg.sprite.Sprite):
    def __init__(self, game, x, y):
        self.game = game
        self._layer = PLAYER_LAYER
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

        self.facing = 'DOWN'
        self.image = self.game.character_spritesheet.get_sprite(1, 0, 15, 24)

        self.rect = self.image.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y

    def update(self):
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
            self.facing = 'LEFT'
        if keys[pg.K_d]:
            self.x_change += PLAYER_SPEED
            self.y_change = 0
            self.facing = 'RIGHT'
        if keys[pg.K_w]:
            self.y_change -= PLAYER_SPEED
            self.x_change = 0
            self.facing = 'UP'
        if keys[pg.K_s]:
            self.y_change += PLAYER_SPEED
            self.x_change = 0
            self.facing = 'DOWN'

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

class TiledMap:
    def __init__(self, filename):
        self.tmxdata = pytmx.load_pygame(filename, pixelalpha=True)
        self.width = self.tmxdata.width * self.tmxdata.tilewidth
        self.height = self.tmxdata.height * self.tmxdata.tileheight
        
    def render(self, surface):
        i = 0
        ti = self.tmxdata.get_tile_image_by_gid
        for layer in self.tmxdata.visible_layers:
            if isinstance(layer, pytmx.TiledTileLayer):
                for x, y, gid, in layer:
                    i += 1
                    self._layer = i
                    tile = ti(gid)
                    if tile:
                        surface.blit(tile, (x * self.tmxdata.tilewidth,
                                            y * self.tmxdata.tileheight))

    def make_map(self):
        temp_surface = pg.Surface((self.width, self.height))
        self.render(temp_surface)
        return temp_surface
import sys
import pygame as pg
from sprites import *
from config import *
from LoadArea import *

class Game:
    def __init__(self):
        pg.init()
        self.clock = pg.time.Clock()
        self.running = True
        self.playing = False

    def intro_menu(self):
        self.state = 'intro_menu'
        self.all_sprites = pg.sprite.LayeredUpdates()
        self.intro = LoadIntro(self)
        while self.state == 'intro_menu':
            self.events()
            self.update()
            self.draw()
            if self.playing == True:
                self.state = 'main'
        
    def events(self):
        # game loop events
        keys = pg.key.get_pressed()
        for event in pg.event.get():
            if event.type == pg.QUIT or keys[pg.K_ESCAPE]:
                self.playing = False
                self.running = False
            elif self.state == 'intro_menu' and keys[pg.K_RETURN]:
                self.intro.pressed_start()
                self.playing = True

    def update(self):
        self.all_sprites.update()

    def draw(self):
        #self.all_sprites.draw(MS)
        self.clock.tick(FPS)

        if self.state == 'intro_menu':
            self.intro.draw()
            
        elif self.state == 'main':
            # game loop draw
            self.area.draw()
        
        self.resized_screen = pg.transform.scale(MS,(WIN_WIDTH, WIN_HEIGHT))
        WIN.blit(self.resized_screen, (0,0))
        pg.display.update()

    def main(self):
        # Game loop
        self.area = LoadArea(self, 'fishing', LOCKE_ASSET)
        while self.playing:
            self.events()
            self.update()
            self.draw()
        self.running = False
    
    def game_over(self):
        pass

g = Game()
g.intro_menu()
while g.running:
    g.main()
pg.QUIT
sys.exit()
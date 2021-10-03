import sys
import pygame as pg
from sprites import *
from config import *
import renderer

class Game:
    def __init__(self):
        pg.init()
        self.clock = pg.time.Clock()
        self.running = True

    def intro_menu(self):
        self.state = 'intro_menu'
        self.new()
        while self.state == 'intro_menu':
            self.events()
            self.update()
            MS.fill(BLUE)
            self.all_sprites.draw(MS)
            self.clock.tick(FPS)

            MS.blit(self.intro_terra.image, self.intro_terra.rect)
            MS.blit(self.intro_locke.image, self.intro_locke.rect)
            self.resized_screen = pg.transform.scale(MS,(WIN_WIDTH, WIN_HEIGHT))
            WIN.blit(self.resized_screen, (0,0))
            pg.display.update()
        
    def new(self):
        self.all_sprites = pg.sprite.LayeredUpdates()
        if self.state == 'intro_menu':
            self.intro_terra = Character('assets/terra/Terra.png', self, INTRO_TERRA_X, INTRO_Y)
            self.intro_locke = Character('assets/locke/Locke.png', self, INTRO_LOCKE_X, INTRO_Y)
            
        elif self.state == 'main':
            self.playing = True
            
            self.map_floor = renderer.Renderer(self, 'assets/fishing_floor.tmx')
            self.map_floor_surface = self.map_floor.make_map()
            self.map_floor_rect = self.map_floor_surface.get_rect()
            
            self.player = Player('assets/terra/Terra.png', self, 1, 1)

            self.map_top = renderer.Renderer(self, 'assets/fishing_top.tmx')
            self.map_top_surface = self.map_top.make_map()
            self.map_top_rect = self.map_top_surface.get_rect()
        
    def events(self):
        # game loop events
        for event in pg.event.get():
            if event.type == pg.QUIT:
                self.playing = False
                self.running = False
            elif pg.key.get_pressed()[pg.K_RETURN]:
                self.state = 'main'

    def update(self):
        self.all_sprites.update()

    def draw(self):
        # game loop draw
        MS.fill(BLUE)
        self.all_sprites.draw(MS)
        self.clock.tick(FPS)
        MS.blit(self.map_floor_surface, self.map_floor_rect)
        MS.blit(self.player.image, self.player.rect)
        MS.blit(self.map_top_surface, self.map_top_rect)
        self.resized_screen = pg.transform.scale(MS,(WIN_WIDTH, WIN_HEIGHT))
        WIN.blit(self.resized_screen, (0,0))
        pg.display.update()

    def main(self):
        # Game loop
        g.new()
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
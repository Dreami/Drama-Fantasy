from renderer import Renderer
from sprites import *

class LoadArea:
    def __init__(self, game, mapName=None, player_asset=False):
        self.game = game
        self.mapName = mapName
        self.mapAsset_b = 'assets/{}_bottom.tmx'.format(self.mapName)
        self.mapAsset_t = 'assets/{}_top.tmx'.format(self.mapName)

        if self.mapName == 'fishing':
            self.spawn_x, self.spawn_y = 3, 3

            self.map_floor = Renderer(self.mapAsset_b)
            self.map_floor_surface = self.map_floor.make_map()
            self.map_floor_rect = self.map_floor_surface.get_rect()
            
            if player_asset:
                self.player = Player(player_asset, self.game, self.spawn_x, self.spawn_y)

            self.map_top = Renderer(self.mapAsset_t)
            self.map_top_surface = self.map_top.make_map()
            self.map_top_rect = self.map_top_surface.get_rect()
        else:
            MS.fill(BLUE)
    
    def draw(self):
        MS.fill(BLACK)
        MS.blit(self.map_floor_surface, self.map_floor_rect)
        
        if self.player:
            MS.blit(self.player.image, self.player.rect)
        
        MS.blit(self.map_top_surface, self.map_top_rect)
        


class LoadIntro(LoadArea):
    def __init__(self, game):
        super().__init__(game)
        self.terra = Character(TERRA_ASSET, self.game, INTRO_TERRA_X, INTRO_Y)
        self.locke = Character(LOCKE_ASSET, self.game, INTRO_LOCKE_X, INTRO_Y)
    
    def pressed_start(self): 
        for i in range(68):
            self.terra.y_change = PLAYER_SPEED
            self.locke.y_change = PLAYER_SPEED
            self.game.update()
            self.game.draw()
    
    def draw(self):
        MS.fill(BLUE)
        MS.blit(self.terra.image, self.terra.rect)
        MS.blit(self.locke.image, self.locke.rect)
        self.resized_screen = pg.transform.scale(MS,(WIN_WIDTH, WIN_HEIGHT))
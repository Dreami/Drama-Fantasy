import pygame as pg

class Control(object):
    def __init__(self):
        self.screen = pg.display.get_surface()
        self.done = False
        self.fps = 60
        self.keys = pg.key.get_pressed()
        self.state_dict = {}
        self.state_name = None
        self.state = None
    
    def setup_states(self, state_dict, start_state):
        self.state_dict = state_dict
        self.state_name = start_state
        self.state = self.state_dict[self.state_name]
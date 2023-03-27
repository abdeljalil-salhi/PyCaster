import pygame as pg
import sys
from settings import *
from map import *
from player import *
from raycasting import *
from object_renderer import *
from sprite_object import *
from object_handler import *
from weapon import *
from sound import *
from pathfinding import *

class Game:
    def __init__(self):
        pg.init()
        if MOUSE:
            pg.mouse.set_visible(False)
        self.screen = pg.display.set_mode(RES)
        self.clock = pg.time.Clock()
        self.delta_time = 1
        self.global_trigger = False
        self.global_event = pg.USEREVENT + 0
        pg.time.set_timer(self.global_event, 40)
        if SOUND:
            self.loop = Sound(self).theme.play()
        self.new_game()
  
    def new_game(self):
        self.map = Map(self)
        self.player = Player(self)
        self.object_renderer = ObjectRenderer(self)
        self.raycasting = RayCasting(self)
        self.crosshair = CrossHair(self)
        self.object_handler = ObjectHandler(self)
        self.weapon = Weapon(self)
        self.sound = Sound(self)
        self.pathfinding = PathFinding(self)
        if SOUND:
            if not self.loop.is_playing():
                self.loop = self.sound.theme.play()

    def update(self):
        self.player.update()
        self.raycasting.update()
        self.object_handler.update()
        self.weapon.update()
        pg.display.flip()
        self.delta_time = self.clock.tick(FPS)
        pg.display.set_caption(f'{self.clock.get_fps():.1f}')
  
    def draw(self):
        if MINIMAP:
            self.screen.fill('black')
            self.map.draw()
            self.player.draw()
        elif not NO_TEXTURES:
            self.screen.fill('black')
            self.object_renderer.draw()
            self.crosshair.draw()
            self.weapon.draw()
  
    def check_events(self):
        for event in pg.event.get():
            if event.type == pg.QUIT or (event.type == pg.KEYDOWN and event.key == pg.K_ESCAPE):
                pg.quit()
                sys.exit()
            elif event.type == pg.KEYDOWN and event.key == pg.K_h:
                self.crosshair.toggle()
            elif event.type == self.global_event:
                self.global_trigger = True
            self.player.single_fire_event(event)
    
    def run(self):
        while True:
            if SOUND:
                if not self.loop.is_playing():
                    self.loop = self.sound.theme.play()
            self.check_events()
            self.update()
            self.draw()
   
if __name__ == '__main__':
    game = Game()
    game.run()

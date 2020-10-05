import sys
import pygame
from view.tilemap import TileMap
from view.cursor import Cursor
from model.gamemap import GameMap
from controler.input_handler import InputHandler


class Level:

    def __init__(self, x, y, tiled):
        pygame.init()
        self.screen = pygame.display.set_mode((x, y), pygame.RESIZABLE)
        self.screen.fill((255, 255, 255))
        self.game_map = GameMap(tiled)
        self.tile_map = TileMap(tiled)
        self.cursor = Cursor()
        self.input_handler = InputHandler(self)

    def set_cursor(self):
        scale_x = self.game_map.x * self.tile_map.scale
        scale_y = self.game_map.y * self.tile_map.scale
        self.cursor.render(self.screen, scale_x, scale_y)

    def render(self):
        self.tile_map.render(self.screen)
        self.set_cursor()

    def execute(self):
        while True:
            for event in pygame.event.get():
                self.input_handler.handle_event(event)


if __name__ == "__main__":
    level = Level(640, 640, "../assets/level1.json")
    level.render()
    level.execute()
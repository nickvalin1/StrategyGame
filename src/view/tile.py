import pygame


class Tile:

    def __init__(self, tile_set, index):
        self.sprite = tile_set[index]
        self.width, self.height = self.sprite.get_size()

    def render(self, screen, x, y, rect):
        coordinates = x * self.width, y * self.height
        screen.blit(self.sprite, coordinates, area=rect)

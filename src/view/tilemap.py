import json
import pygame
from view.tile import Tile


class TileMap:

    def __init__(self, filename):
        with open(filename) as file:
            self.source = json.load(file)
        image = self.source["tilesets"][0]["image"]
        tile_height = self.source["tilesets"][0]["tileheight"]
        tile_width = self.source["tilesets"][0]["tilewidth"]
        self.scale = tile_width
        self.tile_set = self.load_tile_set(image, tile_width, tile_height)
        self.tile_list = []
        for i, code in enumerate(self.source["layers"][0]["data"]):
            tile = Tile(self.tile_set, code)
            x = i // self.source["width"]
            y = i % self.source["width"]
            if y == 0:
                self.tile_list.append([tile])
            else:
                self.tile_list[x].append(tile)

    @staticmethod
    def load_tile_set(filename, width, height):
        image = pygame.image.load(f"../assets/{filename}").convert()
        image_width, image_height = image.get_size()
        tile_set = [None]
        if image_width % width != 0:
            raise RuntimeError("Image width not divisible by tile width")
        elif image_height % height != 0:
            raise RuntimeError("Image height not divisible by tile height")
        for y in range(0, image_height, height):
            for x in range(0, image_width, width):
                tile_source = image.subsurface((x, y, width, height))
                tile_set.append(tile_source)
        return tile_set

    def render(self, screen):
        for y, row in enumerate(self.tile_list):
            for x, tile in enumerate(row):
                tile.render(screen, x, y)
        pygame.display.flip()

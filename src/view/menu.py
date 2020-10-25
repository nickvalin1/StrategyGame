import pygame
import pygame.freetype


class Menu:

    def __init__(self, screen, rect, x_pad=10, y_pad=10):
        self.screen = screen
        self.rect = rect.move(x_pad, y_pad)
        self.font = pygame.freetype.SysFont("lato", 15)
        self.title = "Menu"

    def get_param_text(self, param, value):
        if param == "type":
            return value
        elif param == "move_penalty":
            return "Impassible" if value == 0 else "Hindered" if value < 1 else "Hastened" if value > 1 else None
        elif param == "defense":
            return "Reinforced" if value > 1 else "Compromised" if value < 1 else None
        elif param == "avoid":
            return "Covered" if value > 1 else "Exposed" if value < 1 else None
        else:
            raise NotImplementedError(f"{param} terrain mapping not implemented")

    def get_param_color(self, value):
        if type(value) is str:
            return 0, 0, 0
        elif value <= 0:
            return 0, 0, 0
        elif 0 < value <= .5:
            return 255, 0, 0
        elif .5 < value <= 1:
            return 255, 150, 0
        elif 1 < value <= 1.5:
            return 150, 255, 0
        elif 1.5 < value:
            return 0, 255, 0
        else:
            return 0, 0, 0

    def render(self, tile, unit=None,):
        y_offset = 0
        title, rect = self.font.render(self.title, fgcolor=(0, 0, 0))
        text_length = rect.width // 2
        dest = self.rect.move(self.rect.width // 2 - text_length, y_offset)
        self.screen.blit(title, dest)
        y_offset += 50
        terrain_text = "Terrain: "
        attribute, rect = self.font.render(terrain_text)
        dest = self.rect.move(0, y_offset)
        self.screen.blit(attribute, dest)
        x_offset = 0
        for p, v in tile.get_visible_params():
            text = self.get_param_text(p, v)
            color = self.get_param_color(v)
            if text:
                x_offset += rect.width + 5
                attribute, rect = self.font.render(text, fgcolor=color)
                dest = self.rect.move(x_offset, y_offset)
                self.screen.blit(attribute, dest)

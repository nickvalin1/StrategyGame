import pygame


class Cursor:

    def __init__(self):
        self.sprite = pygame.image.load("../assets/cursor.png").convert_alpha()

    def render(self, screen, x, y):
        screen.blit(self.sprite, (x, y))
        pygame.display.flip()

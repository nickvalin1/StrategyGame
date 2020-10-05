import sys
import pygame


class InputContext:

    def __init__(self, parent):
        self.parent = parent

    def handle_event(self, e):
        event = pygame.event.event_name(e.type)
        if hasattr(self, event):
            return getattr(self, event)(e)
        else:
            return False

    def Quit(self, e):
        # TODO save before exiting
        pygame.quit()
        sys.exit()

    def KeyDown(self, e):
        key = pygame.key.name(e.key)
        if hasattr(self, key):
            return getattr(self, key)(e)
        else:
            return False
